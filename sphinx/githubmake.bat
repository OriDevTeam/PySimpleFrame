:: Simplified way to execute Sphinx default make batch
:: and using PipEnv in another directory

:: Go to back directory and call PipEnv shell and Call default make batch from Sphinx
pushd ..
pipenv run sphinx\\make.bat github
popd

:: Pause to see output
pause