$(document).ready(function (){
    var team = $('#teamid').text();
    
    $.ajax({
        url: 'http://localhost:1555/Board/Items/' + team,
        dataType: 'json',
        success: function (data) {

            $("#data").text(data['something']);
            //alert('daat' + data['something'])
            //items.Queue(data.Queue);
            //items.AnalysisInProgress(data.AnalysisInProgress);
            //items.AnalysisDone(data.AnalysisDone);
            //items.DevInProgress(data.DevInProgress);
            //items.DevDone(data.DevDone);
            //items.TestInProgress(data.TestInProgress);
            //items.TestDone(data.TestDone);
            //items.Members(data.Members);
            //items.TeamClass(data.TeamClass);
            //items.SupportedReleasesText(data.SupportedReleasesText);
            //items.Goal(data.Goal);
            //items.InExpress(data.InExpress);
            //items.InAnalysis(data.InAnalysis);
            //items.InDev(data.InDev);
            //items.InTest(data.InTest);

            //items.AllowedInExpress(data.AllowedInExpress);
            //items.AllowedInAnalysis(data.AllowedInAnalysis);
            //items.AllowedInDev(data.AllowedInDev);
            //items.AllowedInTest(data.AllowedInTest);
            //items.ExpressBackColor(data.ExpressBackColor);
            //items.AnalysisBackColor(data.AnalysisBackColor);
            //items.DevBackColor(data.DevBackColor);
            //items.TestBackColor(data.TestBackColor);

        
        }
        //		,
        //error: function (xhr, ajaxOptions, thrownError) {
        //    alert(xhr.status);
        //    alert(xhr.responseText);
        //    alert(thrownError);
        //}
    });
})