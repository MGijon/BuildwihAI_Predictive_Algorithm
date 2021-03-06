from src.pipeline import Predictor
from src.save_parameters import save_to_json

NUMBER_OF_DAYS = 25

BEGIN_DATE = '2020-07-25'

param_ranges = {
    'beta': (0.0001, 2),  # Rate of transmission
    'sigma': (1 / 24, 1.5),  # Rate of progression
    'gamma': (0.0001, 1),  # Rate of recovery
    'mu_I': (0.0001, 1 / 10),  # Rate of DEATH
    'xi': (0.0001, 0.0001)  # Rate of re-susceptibility
}

genetic_params = {
    'max_gen': 3000,
    'stop_cond': 10000,
    'mut_range': 0.1,
    'p_regen': 0.2,
    'p_mut': 0.4
}

predictor = Predictor(loss_days=35, init_date='2020-06-20', param_ranges=param_ranges, genetic_params=genetic_params)
iterations = predictor.run(verbose=1)

report_data = predictor.report(BEGIN_DATE, NUMBER_OF_DAYS)

seir_data = predictor.generate_data_for_plots(BEGIN_DATE, NUMBER_OF_DAYS)

parameters = '_'.join(['{}-{:.3f}'.format(k, v) for k, v in predictor.best.items()])

save_to_json(seir_data, file_name='seir_{}'.format(parameters))
save_to_json(iterations, file_name='iterations_{}'.format(parameters))
save_to_json(report_data, file_name='report_{}'.format(parameters))
