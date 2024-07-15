from django.shortcuts import render
from .models import lignin
from .models import ncbidb
from .models import pagetab
from .models import taxonomytb
from .models import GeneData
import pandas as pd
from django.http import HttpResponse
import xml.etree.ElementTree as ET
import requests
import xmltodict
from Bio import pairwise2
from Bio.Seq import Seq
import json 
# Create your views here.
def home(request):
    df = pd.DataFrame(list(ncbidb.objects.all().values()))
    tbacteria = df[['org']].drop_duplicates().shape[0]
    tgenes = df[['gene']].drop_duplicates().shape[0]
    tpathways = df[['pathways']].drop_duplicates().shape[0]
    tproduct = df[['product']].drop_duplicates().shape[0]
    stat = {
        'tbac' : str(tbacteria),
        'tgen' : str(tgenes),
        'tpath' : str(tpathways),
        'tpro' : str(tproduct)
    }
    return render(request, 'index.html', stat)

def add(request):
    if request.method == 'POST':
        filess = request.FILES.get("myfile")
        if filess:
            df = pd.read_excel(filess)
            previous = df.dropna()
            previous.iloc[:, 0] = previous.iloc[:, 0].str[3:]
            previous.iloc[:, 0] = previous.iloc[:, 0].str.strip()
            data = lignin.objects.all()
            for index, row in previous.iterrows():
                for i in data:
                    if row[0]==i.bacteria:
                        print(row[2])
                # Create a model instance and assign values from the Excel columns
                my_model = lignin(bacteria=row[0], pathway = row[3], temperature = row[1], ph = row[2])
                # Assign more fields as needed
                #print(row[0])
                # Save the model instance
                my_model.save()
        ncbi_file = request.FILES.get("file2")
        if ncbi_file:
            ncbi = pd.read_csv(ncbi_file)
            ncbi_data = ncbi.loc[:, ['gene', 'organism', 'product', 'translation', 'pathways']]
            for index, row in ncbi_data.iterrows():
                ncbi_model = ncbidb(org = row[1], gene = row[0], product = row[2], sequence = row[3], pathways = row[4])
                ncbi_model.save()
        main_tab = request.FILES.get("file3")
        if main_tab:
            table = pd.read_excel(main_tab)
            table_data = table.loc[:, ['genes', 'organism', 'pathways', 'Taxonomy']]
            for index, row in table_data.iterrows():
                table_model = pagetab(org = row[1], gene = row[0], pathways = row[2], taxonomy = row[3])
                table_model.save()
        main_tab = request.FILES.get("file4")
        if main_tab:
            table = pd.read_excel(main_tab)
            table_data = table.loc[:, ['Organism', 'Taxonomy', 'Taxonomy_1', 'Taxonomy_2', 'Taxonomy_3', 'Taxonomy_4', 'Taxonomy_5', 'Taxonomy_6', 'Taxonomy_7', 'Taxonomy_8']]
            for index, row in table_data.iterrows():
                table_model = taxonomytb(org = row[0], comptax = row[1], taxonomy1 = row[2], taxonomy2 = row[3], taxonomy3 = row[4],
                taxonomy4 = row[5], taxonomy5 = row[6], taxonomy6 = row[7], taxonomy7 = row[8], taxonomy8=[9])
                table_model.save()
        main_tab = request.FILES.get("file5")
        if main_tab:
            table = pd.read_excel(main_tab)
            table_data = table.loc[:, ['gene', 'organism', 'gene_id', 'protein_id', 'product', 'GO_function','GO_process', 'EC_number', 'GO_component', 'function', 'translation', 'pathways']]
            for index, row in table_data.iterrows():
                table_model = GeneData(gene=row[0], organism=row[1], protein_id=row[2], 
                gene_id=row[3], product=row[4], GO_function=row[5], 
                GO_process=row[6], EC_number=row[7], GO_component=row[8], 
                function=row[9], translation=row[10], pathways=row[11])
                table_model.save()
    return render(request, 'data_upload.html')

############################################# Database Search #########################################
def kegg_database(query):
    kegg_list = "https://rest.kegg.jp/find/genes/{}"
    kegg_list = kegg_list.format(query)
    page = requests.get(kegg_list)
    # Split the data string by newline character to get individual lines
    lines = page.text.split('\n')
    # Initialize empty lists to store data for each column
    ids = []
    descriptions = []
    # Process each line and extract data for each column
    for line in lines:
        parts = line.split('\t')  # Split by tab character
        if len(parts) == 2:       # Ensure the line has two parts (ID and Description)
            ids.append(parts[0])
            descriptions.append(parts[1])
    #print(ids)
    # Create the data frame using the extracted data
    file_zip = zip(ids, descriptions)
    return file_zip
def kegg_org():
    kegg_list = "https://rest.kegg.jp/list/organism"
    page = requests.get(kegg_list)
    # Split the data string by newline character to get individual lines
    lines = page.text.split('\n')
    # Initialize empty lists to store data for each column
    ids = []
    descriptions = []
    name = []
    # Process each line and extract data for each column
    for line in lines:
        parts = line.split('\t')  # Split by tab character
        if len(parts) == 4 and "Bacteria" in parts[3]:       # Ensure the line has two parts (ID and Description)
            ids.append(parts[1])
            descriptions.append(parts[3])
            name.append(parts[2])
    return ids,name
# Function to calculate similarity score between two sequences
def calculate_similarity(seq1, seq2):
    alignments = pairwise2.align.globalxx(seq1, seq2, one_alignment_only=True)
    if alignments:
        alignment = alignments[0]
        score = alignment[-3]  # Alignment score
        return score
    else:
        return 0
##########################################################################################################
def search(request):
    query = request.GET.get('query')
    if len(query) == 3:
        query = query
    elif len(query) == 4:
        query = query
    else:
        query = query[1:]
    #print(db)
    if query:
        if len(query) == 0:
            data_dit = {}
        else:
            print(query)
            data = lignin.objects.all()
            ncbi_data = ncbidb.objects.all()
            table_main = pagetab.objects.all()
            for i in data:
                if query in i.pathway:
                    bac = i.bacteria
                pathway_db = i.pathway
                bateria_db = i.bacteria
            data_dit = {
                "pathway":data,
                "search":query,
                "ncbi_db":ncbi_data,
                "maintab": table_main
            }
    else:
        data_dit = {}
    return render(request, "search_result.html", data_dit)

def filter_data(request):
    sel1 = request.GET.get('dropdown1')
    sel2 = request.GET.get('dropdown2')
    print(sel1, sel2)
    if len(sel1) == 3:
        sel1 = sel1
    elif len(query) == 4:
        sel1 = sel1
    else:
        sel1 = sel1[1:]
    #print(db)
    if sel1:
        if len(sel1) == 0:
            data_dit = {}
        else:
            print(sel1)
            data = lignin.objects.all()
            ncbi_data = ncbidb.objects.all()
            table_main = pagetab.objects.all()
            for i in data:
                if query in i.pathway:
                    bac = i.bacteria
                pathway_db = i.pathway
                bateria_db = i.bacteria
            data_dit = {
                "pathway":data,
                "search":sel1,
                "ncbi_db":ncbi_data,
                "maintab": table_main
            }
    else:
        data_dit = {}
    return render(request, "search_result.html", data_dit)

def alignment(request):
    return render(request, "seqalign.html")

def seqalign(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        print(user_input)
    ncbi_data = ncbidb.objects.all()
    sequence_list = ncbidb.objects.values_list('sequence', flat=True)
    # Calculate similarity scores for all sequences
    similarity_scores = {}
    for sequence in sequence_list:
        similarity_scores[sequence] = calculate_similarity(user_input, sequence)

    # Find sequences with similarity greater than 90%
    similar_sequences = [seq for seq, score in similarity_scores.items() if score >= 0.9 * len(user_input)]
    data_dit = {
        "ncbi_data":ncbi_data,
        "query":similar_sequences
    }
    # Print the similar sequences and their scores

    return render(request, "alignres.html", data_dit)


def kegg(request):
    query = request.GET["search"]
    query = query.replace(" ","+")
    print(query)
    kegg_list = "https://rest.kegg.jp/find/genes/{}"
    kegg_list = kegg_list.format(query)
    page = requests.get(kegg_list)
    # Split the data string by newline character to get individual lines
    lines = page.text.split('\n')
    # Initialize empty lists to store data for each column
    ids = []
    descriptions = []
    # Process each line and extract data for each column
    for line in lines:
        parts = line.split('\t')  # Split by tab character
        if len(parts) == 2:       # Ensure the line has two parts (ID and Description)
            ids.append(parts[0])
            descriptions.append(parts[1])
    print(ids)
    # Create the data frame using the extracted data
    file_zip = zip(ids, descriptions)
    data = {
        'ID': file_zip
    }
    return render(request, "kegg_search.html", data)

def kegg_page(request):
    return render(request, "kegg.html")

def resultsdetails(request,org):
    print(org)
    data = GeneData.objects.filter(organism = org).values()
    disp = {
        'comR' : data,
        'organism' : org
    }
    return render(request, "resultsdetails.html", disp)
def genesdetails(request,gene):
    print(gene)
    data = GeneData.objects.filter(gene = gene).values()
    df = pd.DataFrame(list(GeneData.objects.filter(gene = gene).values()))
    print(df)
    disp = {
        'comR' : data,
        'gene' : gene
    }
    return render(request, "genesdetails.html", disp)

def taxonomytbdata(request):
    data = taxonomytb.objects.all()
    numbers = ["=100", ">80", "<80"]
    disp = {
        'taxo' : data,
        'numbers' : numbers
    }
    return render(request, "taxonomy.html", disp)

def taxonomytbpres(request):
    query1 = request.GET.get('phylum')
    query2 = request.GET.get('class')
    query3 = request.GET.get('Order')
    query4 = request.GET.get('family')
    query5 = request.GET.get('genus')
    numper = request.GET.get('percen')
    symb = numper[0]
    numper = int(numper[1:])
    #query = f'''{query1};{query2};{query3};{query4};{query5}'''
    if query1 and query2 and query3 and query4 and query5:
        query = f"{query1}; {query2}; {query3}; {query4}; {query5}"
    elif query1 and query2 and query3 and query4:
        query = f"{query1}; {query2}; {query3}; {query4}"
    elif query1 and query2 and query3:
        query = f"{query1}; {query2}; {query3}"
    elif query1 and query2:
        query = f"{query1}; {query2}"
    else:
        query = query1
    print(query)
    data = taxonomytb.objects.all()
    df = pd.DataFrame(list(taxonomytb.objects.all().values()))
    #print(df)
    filtered_df = df[df['comptax'].str.contains(query)]
    query_in_db = filtered_df[['comptax']]
    #print(filtered_df[['comptax']])
    query_in_db.drop_duplicates(subset=['comptax'], keep='first')
    ncbidbdata = pd.DataFrame(list(pagetab.objects.all().values()))
    # Splitting genes, grouping by 'Pathways Name', and counting unique genes
    ncbidbdata['gene'] = ncbidbdata['gene'].apply(lambda x: x.split(', '))
    pathway_group = ncbidbdata.explode('gene').groupby('pathways')['gene'].nunique()

    # Adding 'Total Genes in Pathway' column
    ncbidbdata['Total Genes in Pathway'] = ncbidbdata['pathways'].map(pathway_group)

    # Calculate the percentage of genes with respect to the total genes in each pathway
    ncbidbdata['Percentage'] = (ncbidbdata['gene'].apply(len) / ncbidbdata['Total Genes in Pathway']) * 100

    # Display the updated data with the added columns
    #print(ncbidbdata)
    final_data = ncbidbdata[ncbidbdata['taxonomy'].isin(query_in_db['comptax'])]
    if symb == '>':
        final_data = final_data[final_data['Percentage'] >= numper]
    elif symb == '<':
        final_data = final_data[final_data['Percentage'] <= numper]
    else:
        final_data = final_data[final_data['Percentage'] == numper]
    json_records = final_data.reset_index().to_json(orient ='records') 
    datap = [] 
    datap = json.loads(json_records) 
    context = {'d': datap} 
    #print(final_data)
    print(type(query_in_db))
    return render(request, "taxonomyres.html", context)