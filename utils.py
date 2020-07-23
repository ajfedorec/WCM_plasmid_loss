

def generate_integrate_inputs(bioreactor, strain_list):
    species_list = []
    y0 = []

    bioreactor.sample_initial_species()
    B_species_keys, B_y0 = bioreactor.get_initial_species()
    bioreactor.sample_parameters()

    species_list += B_species_keys
    y0 += B_y0

    for strain in strain_list:
        strain.sample_initial_species()
        strain.sample_parameters()
        strain.categorise_species()
        strain_species_keys, strain_y0 = strain.get_initial_species()
        species_list += strain_species_keys
        y0 += strain_y0

    return species_list, y0