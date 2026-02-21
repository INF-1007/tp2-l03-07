"""
TP2 – Exercice 1 : Analyse des modules de la station spatiale ORBIT-X

Objectif :
Analyser les modules de la station afin d'extraire des statistiques utiles
pour la planification de la maintenance.

Un module est représenté par :
    nom_module : (cout_maintenance, temps_intervention, criticite)

Exemple :
modules = {
    'Laboratoire': (120, 15, 8),
    'Habitat': (200, 10, 9),
    'Observatoire': (150, 20, 6)
}
"""
import math
# -------------------------------------------------------------------
# 1) Analyse des modules
# -------------------------------------------------------------------


def analyser_modules(modules):
    """
    Analyse les modules de la station.

    Args:
        modules (dict): {nom_module: (cout, temps, criticite)}

    Returns:
        dict contenant :
            - 'module_plus_critique' : str ou None
            - 'cout_moyen' : float
            - 'temps_moyen' : float
    """

    stats = {
        'module_plus_critique': None,
        'cout_moyen': 0,
        'temps_moyen': 0
    }

    # TODO 1 : Gérer le cas où le dictionnaire est vide
    # Dans ce cas, retourner stats tel quel
    if len(modules) == 0:
        return stats

    # TODO 2 : Parcourir les modules
    # - Identifier le module ayant le meilleur ratio criticite / temps_intervention
    #   ⚠️ Ignorer les modules avec temps_intervention == 0
    #   ⚠️ En cas d’égalité, conserver le premier module rencontré
    ratio_meilleur = max([m_stats[2] / m_stats[1] for m_stats in modules.values() if m_stats[1] > 0]) 

    for module, m_stats in modules.items():
        if m_stats[1] > 0:
            if m_stats[2] / m_stats[1] == ratio_meilleur:
                stats['module_plus_critique'] = module
                break
            

    # TODO 3 : Calculer les moyennes
    # - cout_moyen = somme_couts / nombre_modules
    # - temps_moyen = somme_temps / nombre_modules
    somme_couts = math.fsum([m_stats[0] for m_stats in modules.values()])
    somme_temps = math.fsum([m_stats[1] for m_stats in modules.values()])

    stats['cout_moyen'] = somme_couts / len(modules)
    stats['temps_moyen'] = somme_temps / len(modules)

    return stats

# -------------------------------------------------------------------
# 2) Regroupement des modules par type
# -------------------------------------------------------------------


def regrouper_modules_par_type(modules, types):
    """
    Regroupe les modules par type.

    Args:
        modules (dict): dictionnaire des modules
        types (dict): {nom_module: type}

    Returns:
        dict: {type: [liste des modules]}
    """

    modules_par_type = {}

    # TODO :
    # Pour chaque module :
    #   - Vérifier s’il existe dans le dictionnaire types
    #   - Ajouter le module dans la liste correspondant à son type
    #   - Créer la liste si elle n’existe pas encore
    # ⚠️ Ignorer silencieusement les modules sans type
    for module in modules.keys():
        if module in types:
            if not types[module] in modules_par_type:
                modules_par_type[types[module]] = [module]
            else:
                modules_par_type[types[module]].append(module)

    return modules_par_type

# -------------------------------------------------------------------
# 3) Calcul du cout total
# -------------------------------------------------------------------


def calculer_cout_total(modules, interventions):
    """
    Calcule le coût total de maintenance prévu.

    Args:
        modules (dict): {nom_module: (cout, temps, criticite)}
        interventions (dict): {nom_module: nombre_interventions}

    Returns:
        float: coût total
    """

    cout_total = 0.0

    # TODO :
    # Pour chaque module dans interventions :
    #   - Vérifier qu’il existe dans modules
    #   - Ajouter à cout_total le cout total de maintenance du module étant donné le nombre d'interventions
    # ⚠️ Ignorer les modules absents de modules

    for module, stats in modules.items():
        if module in interventions:
            cout_total += stats[0] * interventions.get(module)

    return cout_total

# -------------------------------------------------------------------
# TESTS main
# -------------------------------------------------------------------


if __name__ == "__main__":
    modules_test = {
        'Laboratoire': (120, 15, 8),
        'Habitat': (200, 10, 9),
        'Observatoire': (150, 20, 6)
    }

    types_test = {
        'Laboratoire': 'science',
        'Habitat': 'vie',
        'Observatoire': 'science'
    }

    interventions_test = {
        'Laboratoire': 2,
        'Habitat': 1
    }

    print(analyser_modules(modules_test))
    print(regrouper_modules_par_type(modules_test, types_test))
    print(calculer_cout_total(modules_test, interventions_test))
