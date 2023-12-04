function cmcStates = importCMCStatesFileToDataset(filename, startRow, endRow)
% Initialize variables.
delimiter = '\t';
if nargin<=2
    startRow = 8;
    endRow = inf;
end

% Format string for each line of text:
formatSpec = '%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%[^\n\r]';

% Open the text file.
fileID = fopen(filename,'r');

% Read columns of data according to format string.
dataArray = textscan(fileID, formatSpec, endRow(1)-startRow(1)+1, 'Delimiter', delimiter, 'EmptyValue' ,NaN,'HeaderLines', startRow(1)-1, 'ReturnOnError', false);
for block=2:length(startRow)
    frewind(fileID);
    dataArrayBlock = textscan(fileID, formatSpec, endRow(block)-startRow(block)+1, 'Delimiter', delimiter, 'EmptyValue' ,NaN,'HeaderLines', startRow(block)-1, 'ReturnOnError', false);
    for col=1:length(dataArray)
        dataArray{col} = [dataArray{col};dataArrayBlock{col}];
    end
end

% Close the text file.
fclose(fileID);

% Create output variable
cmcStates = dataset(dataArray{1:end-1}, 'VarNames', {'time','pelvistilt','pelvislist','pelvisrotation','pelvistx','pelvisty','pelvistz','hipflexionr','hipadductionr','hiprotationr','kneeangler','kneeanglerbeta','ankleangler','subtalarangler','mtpangler','hipflexionl','hipadductionl','hiprotationl','kneeanglel','kneeanglelbeta','ankleanglel','subtalaranglel','mtpanglel','lumbarextension','lumbarbending','lumbarrotation','armflexr','armaddr','armrotr','elbowflexr','prosupr','wristflexr','wristdevr','armflexl','armaddl','armrotl','elbowflexl','prosupl','wristflexl','wristdevl','pelvistiltu','pelvislistu','pelvisrotationu','pelvistxu','pelvistyu','pelvistzu','hipflexionru','hipadductionru','hiprotationru','kneeangleru','kneeanglerbetau','ankleangleru','subtalarangleru','mtpangleru','hipflexionlu','hipadductionlu','hiprotationlu','kneeanglelu','kneeanglelbetau','ankleanglelu','subtalaranglelu','mtpanglelu','lumbarextensionu','lumbarbendingu','lumbarrotationu','armflexru','armaddru','armrotru','elbowflexru','prosupru','wristflexru','wristdevru','armflexlu','armaddlu','armrotlu','elbowflexlu','prosuplu','wristflexlu','wristdevlu','addbrevractivation','addlongractivation','addlongrfiberlength','addmagDistractivation','addmagIschractivation','addmagIschrfiberlength','addmagMidractivation','addmagProxractivation','bflhractivation','bflhrfiberlength','bfshractivation','edlractivation','edlrfiberlength','ehlractivation','ehlrfiberlength','fdlractivation','fdlrfiberlength','fhlractivation','fhlrfiberlength','gaslatractivation','gaslatrfiberlength','gasmedractivation','gasmedrfiberlength','glmax1ractivation','glmax2ractivation','glmax3ractivation','glmed1ractivation','glmed2ractivation','glmed3ractivation','glmin1ractivation','glmin2ractivation','glmin3ractivation','glmin3rfiberlength','gracractivation','iliacusractivation','perbrevractivation','perbrevrfiberlength','perlongractivation','perlongrfiberlength','piriractivation','pirirfiberlength','psoasractivation','recfemractivation','recfemrfiberlength','sartractivation','semimemractivation','semimemrfiberlength','semitenractivation','semitenrfiberlength','soleusractivation','soleusrfiberlength','tflractivation','tflrfiberlength','tibantractivation','tibantrfiberlength','tibpostractivation','tibpostrfiberlength','vasintractivation','vasintrfiberlength','vaslatractivation','vaslatrfiberlength','vasmedractivation','vasmedrfiberlength','addbrevlactivation','addlonglactivation','addlonglfiberlength','addmagDistlactivation','addmagIschlactivation','addmagIschlfiberlength','addmagMidlactivation','addmagProxlactivation','bflhlactivation','bflhlfiberlength','bfshlactivation','edllactivation','edllfiberlength','ehllactivation','ehllfiberlength','fdllactivation','fdllfiberlength','fhllactivation','fhllfiberlength','gaslatlactivation','gaslatlfiberlength','gasmedlactivation','gasmedlfiberlength','glmax1lactivation','glmax2lactivation','glmax3lactivation','glmed1lactivation','glmed2lactivation','glmed3lactivation','glmin1lactivation','glmin2lactivation','glmin3lactivation','glmin3lfiberlength','graclactivation','iliacuslactivation','perbrevlactivation','perbrevlfiberlength','perlonglactivation','perlonglfiberlength','pirilactivation','pirilfiberlength','psoaslactivation','recfemlactivation','recfemlfiberlength','sartlactivation','semimemlactivation','semimemlfiberlength','semitenlactivation','semitenlfiberlength','soleuslactivation','soleuslfiberlength','tfllactivation','tfllfiberlength','tibantlactivation','tibantlfiberlength','tibpostlactivation','tibpostlfiberlength','vasintlactivation','vasintlfiberlength','vaslatlactivation','vaslatlfiberlength','vasmedlactivation','vasmedlfiberlength'});
