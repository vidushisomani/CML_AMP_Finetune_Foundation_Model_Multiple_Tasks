from amp_3_job_fine_tune.distributed_peft_scripts.common import accelerate_launcher

# Launch accelerate cli tool via a wrapper script that sets up distribution configs
accelerate_launcher.launch_distributed_script("amp_3_job_fine_tune/distributed_peft_scripts/task_detox_fine_tuner.py")