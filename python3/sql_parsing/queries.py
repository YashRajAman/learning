queries = [
    """
    INSERT INTO $$DB_STG.V_NY_ST_HCB_APCD_DQ_CLM_FILE ( NY_ST_HCB_APCD_DQ_CLM_FILE_GID ,RECORD_TYP ,RECORD_TYP_VERSION ,CLAIM_TYP ,UCK_INFO_PRFIX ,UCK_INFO_EC_ID_XX ,UCK_INFO_SEG_NBR ,REC_SEQ ,SBMTR_SRVC_LINE_NBR ,CLM0001 ,CLM0002 ,CLM0003 ,CLM0004 ,CLM0005 ,CLM0006 ,CLM0007 ,CLM0008 ,CLM0009 ,CLM0010 ,CLM0011 ,CLM0012 ,CLM0013 ,CLM0014 ,CLM0015 ,CLM0016 ,CLM0017 ,CLM0018 ,CLM0019 ,CLM0020 ,CLM0021 ,CLM0022 ,CLM0023 ,CLM0024 ,CLM0025 ,CLM0026 ,CLM0027, CLM0028 , CLM0029 , CLM0030 , CLM0031 , CLM0032 , CLM0033 , CLM0034 , CLM0035 , CLM0036 , CLM0037 , CLM0038 , CLM0039 , CLM0040 , CLM0041 , CLM0042 , CLM0043 , CLM0044 , CLM0045 , CLM0046 , CLM0047 , CLM0048 , CLM0049 , CLM0050 , CLM0051 , CLM0052 , CLM0053 , CLM0054 , CLM0055 , CLM0056 , CLM0057 , CLM0058 , CLM0059 , CLM0060 , CLM0061 , CLM0062 , CLM0063 , CLM0064 , CLM0065 , CLM0066 , CLM0067 , CLM0068 , CLM0069 , CLM0070 , CLM0071 , CLM0072 , CLM0073 , CLM0074 , CLM0075 , CLM0076 , CLM0077 , CLM0078 , CLM0079 , CLM0080 , CLM0081 , CLM0082 , CLM0083 , CLM0084 , CLM0085 , CLM0086 , CLM0087 , CLM0088 , CLM0089 , CLM0090 , CLM0091 , CLM0092 , CLM0093 , CLM0094 ,RPT_EXECN_DT ,RPT_TYP_CD ,RPT_PRD_STRT_DT ,RPT_PRD_END_DT ,INPUT_FILE_NM ,PLAT_FORM_CD ,RPT_ST_CD ,REC_HIST_GID ,REC_ADD_TS ) SELECT MAX_NY_ST_HCB_APCD_DQ_CLM_FILE_GID + ROW_NUMBER() OVER(ORDER BY UCK_INFO_PRFIX, UCK_INFO_EC_ID_XX , SEQ_NO,UCK_INFO_SEG_NBR ) AS NY_ST_HCB_APCD_DQ_CLM_FILE_GID , TRIM( SUBSTR( LINE_DATA, 1 , 12 )) AS CSV_0800_RECORD_TYP , TRIM( SUBSTR( LINE_DATA, 13 , 5 )) AS CSV_0800_RECORD_TYP_VERSION , TRIM( SUBSTR( LINE_DATA, 18 , 8 )) AS CSV_0800_CLAIM_TYP , TRIM( SUBSTR( LINE_DATA, 26 , 1 )) AS UCK_INFO_PRFIX , TRIM( SUBSTR( LINE_DATA, 27 , 8 )) AS UCK_INFO_EC_ID_XX , TRIM( SUBSTR( LINE_DATA, 35 , 2 )) AS UCK_INFO_SEG_NBR , TRIM( SUBSTR( LINE_DATA, 37 , 4 )) AS CSV_0800_REC_SEQ , TRIM( SUBSTR( LINE_DATA, 41 , 9 )) AS CSV_0800_SBMT_SRVC_LN_NO , TRIM( SUBSTR( LINE_DATA, 50 , 1 )) AS CSV_0800_REND_PRVDR_ENTY_TYP_QLFR_CD , TRIM( SUBSTR( LINE_DATA, 51 , 60 )) AS CSV_0800_REND_PRVDR_LAST_NM , TRIM( SUBSTR( LINE_DATA, 111 , 35 )) AS CSV_0800_REND_PRVDR_FRST_NM , TRIM( SUBSTR( LINE_DATA, 146 , 25 )) AS CSV_0800_REND_PRVDR_MDL_NM , TRIM( SUBSTR( LINE_DATA, 171 , 10 )) AS CSV_0800_REND_PRVDR_SFX_NM , TRIM( SUBSTR( LINE_DATA, 181 , 80 )) AS CSV_0800_REND_PRVDR_NPI_TXT , TRIM( SUBSTR( LINE_DATA, 261 , 50 )) AS CSV_0800_REND_PRVDR_SPCLT_INFO_REF_ID , TRIM( SUBSTR( LINE_DATA, 311 , 3 )) AS CSV_0800_REND_PREV_SCNDRY_ID_RFRNC_ID_QLFR_01_CD , TRIM( SUBSTR( LINE_DATA, 314 , 50 )) AS CSV_0800_REND_PRVDR_SCNDRY_ID_REF_01_ID , TRIM( SUBSTR( LINE_DATA, 364 , 50 )) AS CSV_0800_OTHER_PAYER_PRM_REND_PRVDR_SCNDRY_01_ID , TRIM( SUBSTR( LINE_DATA, 414 , 3 )) AS CSV_0800_REND_PREV_SCNDRY_ID_RFRNC_ID_QLFR_02_CD , TRIM( SUBSTR( LINE_DATA, 417 , 50 )) AS CSV_0800_REND_PRVDR_SCNDRY_ID_REF_02_ID , TRIM( SUBSTR( LINE_DATA, 467 , 50 )) AS CSV_0800_OTHER_PAYER_PRM_REND_PRVDR_SCNDRY_02_ID , TRIM( SUBSTR( LINE_DATA, 517 , 3 )) AS CSV_0800_REND_PREV_SCNDRY_ID_RFRNC_ID_QLFR_03_CD , TRIM( SUBSTR( LINE_DATA, 520 , 50 )) AS CSV_0800_REND_PRVDR_SCNDRY_ID_REF_03_ID , TRIM( SUBSTR( LINE_DATA, 570 , 50 )) AS CSV_0800_OTHER_PAYER_PRM_REND_PRVDR_SCNDRY_03_ID , TRIM( SUBSTR( LINE_DATA, 620 , 1 )) AS CSV_0800_PRCHS_SRVC_PRVDR_NM_ENTY_TYP_QLFR_CD , TRIM( SUBSTR( LINE_DATA, 621 , 80 )) AS CSV_0800_PRCHS_SRVC_NPI , TRIM( SUBSTR( LINE_DATA, 701 , 3 )) AS CSV_0800_PRCHS_SRVC_PRVDR_SCNDRY_ID_QLFR_01_CD , TRIM( SUBSTR( LINE_DATA, 704 , 50 )) AS CSV_0800_PRCHS_SRVC_PRVDR_SCNDRY_01_ID , TRIM( SUBSTR( LINE_DATA, 754 , 50 )) AS CSV_0800_OTHER_PAYER_PRM_01_ID , TRIM( SUBSTR( LINE_DATA, 804 , 3 )) AS CSV_0800_PRCHS_SRVC_PRVDR_SCNDRY_ID_QLFR_02_CD , TRIM( SUBSTR( LINE_DATA, 807 , 50 )) AS CSV_0800_PRCHS_SRVC_PRVDR_SCNDRY_02_ID , TRIM( SUBSTR( LINE_DATA, 857 , 50 )) AS CSV_0800_OTHER_PAYER_PRM_02_ID , TRIM( SUBSTR( LINE_DATA, 907 , 60 )) AS CSV_0800_SRVC_FCLTY_LCTN_NM , TRIM( SUBSTR( LINE_DATA, 967 , 80 )) AS CSV_0800_SRVC_FCLTY_NPI , TRIM( SUBSTR( LINE_DATA, 1047 , 55 )) AS CSV_0800_SRVC_FCLTY_LCTN_ADDR_LINE_1_TXT , TRIM( SUBSTR( LINE_DATA, 1102 , 55 )) AS CSV_0800_SRVC_FCLTY_LCTN_ADDR_LINE_2_TXT , TRIM( SUBSTR( LINE_DATA, 1157 , 30 )) AS CSV_0800_SRVC_FCLTY_LCTN_CITY_NM , TRIM( SUBSTR( LINE_DATA, 1187 , 2 )) AS CSV_0800_SRVC_FCLTY_LCTN_ST_CD , TRIM( SUBSTR( LINE_DATA, 1189 , 15 )) AS CSV_0800_SRVC_FCLTY_LCTN_ZIP_CD , TRIM( SUBSTR( LINE_DATA, 1204 , 3 )) AS CSV_0800_SRVC_FCLTY_LCTN_CNTRY_CD , TRIM( SUBSTR( LINE_DATA, 1207 , 60 )) AS CSV_0800_SRVC_FCLTY_LCTN_CNTRY_SUBDV_CD , TRIM( SUBSTR( LINE_DATA, 1267 , 3 )) AS CSV_0800_SRVC_FCLTY_LCTN_ID_QLFR_01_CD , TRIM( SUBSTR( LINE_DATA, 1270 , 50 )) AS CSV_0800_LAB_OR_FCLTY_01_SCNDRY_01_ID , TRIM( SUBSTR( LINE_DATA, 1320 , 3 )) AS CSV_0800_SRVC_FCLTY_LCTN_ID_QLFR_02_CD , TRIM( SUBSTR( LINE_DATA, 1323 , 50 )) AS CSV_0800_LAB_OR_FCLTY_01_SCNDRY_02_ID , TRIM( SUBSTR( LINE_DATA, 1373 , 3 )) AS CSV_0800_SRVC_FCLTY_LCTN_ID_QLFR_03_CD , TRIM( SUBSTR( LINE_DATA, 1376 , 50 )) AS CSV_0800_LAB_OR_FCLTY_01_SCNDRY_03_ID , TRIM( SUBSTR( LINE_DATA, 1426 , 60 )) AS CSV_0800_SPVSG_SURGICAL_LAST_NM , TRIM( SUBSTR( LINE_DATA, 1486 , 35 )) AS CSV_0800_SPVSG_SURGICAL_FRST_NM , TRIM( SUBSTR( LINE_DATA, 1521 , 25 )) AS CSV_0800_SPVSG_SURGICAL_MDL_NM , TRIM( SUBSTR( LINE_DATA, 1546 , 10 )) AS CSV_0800_SPVSG_SURGICAL_SFX_NM , TRIM( SUBSTR( LINE_DATA, 1556 , 80 )) AS CSV_0800_SPVSG_SURGICAL_ID , TRIM( SUBSTR( LINE_DATA, 1636 , 3 )) AS CSV_0800_SPVSG_PRVDR_SCNDRY_ID_QLFR_01_CD , TRIM( SUBSTR( LINE_DATA, 1639 , 50 )) AS CSV_0800_SPVSG_PRVDR_SCNDRY_ID_REF_01_ID , TRIM( SUBSTR( LINE_DATA, 1689 , 50 )) AS CSV_0800_OTHER_PAYER_PRM_SPVSG_PREV_SCNDRY_01_ID , TRIM( SUBSTR( LINE_DATA, 1739 , 3 )) AS CSV_0800_SPVSG_PRVDR_SCNDRY_ID_QLFR_02_CD , TRIM( SUBSTR( LINE_DATA, 1742 , 50 )) AS CSV_0800_SPVSG_PRVDR_SCNDRY_ID_REF_02_ID , TRIM( SUBSTR( LINE_DATA, 1792 , 50 )) AS CSV_0800_OTHER_PAYER_PRM_SPVSG_PREV_SCNDRY_02_ID , TRIM( SUBSTR( LINE_DATA, 1842 , 3 )) AS CSV_0800_SPVSG_PRVDR_SCNDRY_ID_QLFR_03_CD , TRIM( SUBSTR( LINE_DATA, 1845 , 50 )) AS CSV_0800_SPVSG_PRVDR_SCNDRY_ID_REF_03_ID , TRIM( SUBSTR( LINE_DATA, 1895 , 50 )) AS CSV_0800_OTHER_PAYER_PRM_SPVSG_PREV_SCNDRY_03_ID , TRIM( SUBSTR( LINE_DATA, 1945 , 60 )) AS CSV_0800_ORDR_PRVDR_LAST_NM , TRIM( SUBSTR( LINE_DATA, 2005 , 35 )) AS CSV_0800_ORDR_PRVDR_FRST_NM , TRIM( SUBSTR( LINE_DATA, 2040 , 25 )) AS CSV_0800_ORDR_PRVDR_MDL_NM , TRIM( SUBSTR( LINE_DATA, 2065 , 10 )) AS CSV_0800_ORDR_PRVDR_SFX_NM , TRIM( SUBSTR( LINE_DATA, 2075 , 80 )) AS CSV_0800_ORDR_PRVDR_NPI , TRIM( SUBSTR( LINE_DATA, 2155 , 55 )) AS CSV_0800_ORDR_PRVDR_ADDR_LINE_1_TXT , TRIM( SUBSTR( LINE_DATA, 2210 , 55 )) AS CSV_0800_ORDR_PRVDR_ADDR_LINE_2_TXT , TRIM( SUBSTR( LINE_DATA, 2265 , 30 )) AS CSV_0800_ORDR_PRVDR_CITY_NM , TRIM( SUBSTR( LINE_DATA, 2295 , 2 )) AS CSV_0800_ORDR_PRVDR_ST_CD , TRIM( SUBSTR( LINE_DATA, 2297 , 15 )) AS CSV_0800_ORDR_PRVDR_ZIP_CD , TRIM( SUBSTR( LINE_DATA, 2312 , 3 )) AS CSV_0800_ORDR_PRVDR_CNTRY_CD , TRIM( SUBSTR( LINE_DATA, 2315 , 3 )) AS CSV_0800_ORDR_PRVDR_CNTRY_SUBDV_CD , TRIM( SUBSTR( LINE_DATA, 2318 , 3 )) AS CSV_0800_ORDR_PRVDR_ID_QLFR_01_CD , TRIM( SUBSTR( LINE_DATA, 2321 , 50 )) AS CSV_0800_ORDR_PRVDR_01_ID , TRIM( SUBSTR( LINE_DATA, 2371 , 3 )) AS CSV_0800_ORDR_PRVDR_ID_QLFR_02_CD , TRIM( SUBSTR( LINE_DATA, 2374 , 50 )) AS CSV_0800_ORDR_PRVDR_02_ID , TRIM( SUBSTR( LINE_DATA, 2424 , 60 )) AS CSV_0800_ORDR_PRVDR_CNTCT_NM , TRIM( SUBSTR( LINE_DATA, 2484 , 2 )) AS CSV_0800_CMNCT_NBR_QLFR_01_CD , TRIM( SUBSTR( LINE_DATA, 2486 , 256 )) AS CSV_0800_CMNCT_1_TXT , TRIM( SUBSTR( LINE_DATA, 2742 , 2 )) AS CSV_0800_CMNCT_NBR_QLFR_02_CD , TRIM( SUBSTR( LINE_DATA, 2744 , 256 )) AS CSV_0800_CMNCT_2_TXT , TRIM( SUBSTR( LINE_DATA, 3000 , 2 )) AS CSV_0800_CMNCT_NBR_QLFR_03_CD , TRIM( SUBSTR( LINE_DATA, 3002 , 256 )) AS CSV_0800_CMNCT_3_TXT , TRIM( SUBSTR( LINE_DATA, 3258 , 60 )) AS CSV_0800_RFRN_PRVDR_LAST_01_NM , TRIM( SUBSTR( LINE_DATA, 3318 , 35 )) AS CSV_0800_REF_PRVDR_FRST_01_NM , TRIM( SUBSTR( LINE_DATA, 3353 , 25 )) AS CSV_0800_RFRN_PRVDR_MDL_01_NM , TRIM( SUBSTR( LINE_DATA, 3378 , 10 )) AS CSV_0800_RFRN_PRVDR_SFX_01_NM , TRIM( SUBSTR( LINE_DATA, 3388 , 10 )) AS CSV_0800_RFRN_PRVDR_TIN_SSN_01_TXT , TRIM( SUBSTR( LINE_DATA, 3398 , 3 )) AS CSV_0800_REF_PREV_SCNDRY_ID_RFRNC_ID_QLFR_01_CD , TRIM( SUBSTR( LINE_DATA, 3401 , 50 )) AS CSV_0800_RFRN_PRVDR_SCNDRY_ID_REF_01_ID , TRIM( SUBSTR( LINE_DATA, 3451 , 3 )) AS CSV_0800_REF_PREV_SCNDRY_ID_RFRNC_ID_QLFR_02_CD , TRIM( SUBSTR( LINE_DATA, 3454 , 50 )) AS CSV_0800_RFRN_PRVDR_SCNDRY_ID_REF_02_ID , TRIM( SUBSTR( LINE_DATA, 3504 , 60 )) AS CSV_0800_RFRN_PRVDR_LAST_02_NM , TRIM( SUBSTR( LINE_DATA, 3564 , 35 )) AS CSV_0800_REF_PRVDR_FRST_02_NM , TRIM( SUBSTR( LINE_DATA, 3599 , 25 )) AS CSV_0800_RFRN_PRVDR_MDL_02_NM , TRIM( SUBSTR( LINE_DATA, 3624 , 10 )) AS CSV_0800_RFRN_PRVDR_SFX_02_NM , TRIM( SUBSTR( LINE_DATA, 3634 , 10 )) AS CSV_0800_RFRN_PRVDR_TIN_SSN_02_TXT , TRIM( SUBSTR( LINE_DATA, 3644 , 3 )) AS CSV_0800_REF_PREV_SCNDRY_ID_RFRNC_ID_QLFR_03_CD , TRIM( SUBSTR( LINE_DATA, 3647 , 50 )) AS CSV_0800_RFRN_PRVDR_SCNDRY_ID_REF_03_ID , TRIM( SUBSTR( LINE_DATA, 3697 , 3 )) AS CSV_0800_REF_PREV_SCNDRY_ID_RFRNC_ID_QLFR_04_CD , TRIM( SUBSTR( LINE_DATA, 3700 , 50 )) AS CSV_0800_RFRN_PRVDR_SCNDRY_ID_REF_04_ID ,CURRENT_DATE ,'D' ,AUDT.RPT_STRT_DT ,AUDT.RPT_END_DT ,INPUT_FILE_NM ,'$$PLAT_FORM_CD' AS PLAT_FORM_CD ,'$$RPT_ST_CD' AS RPT_ST_CD ,$$PRCS_RUN_GID AS REC_HIST_GID,                                                                                                  CURRENT_TIMESTAMP(0)
    FROM $$DB_LND.V_APCD_NY_CLM_NG_PRFSN_DQ CROSS JOIN VOL_APCD_CLM_AUDT AUDT CROSS JOIN (SELECT COALESCE(MAX(NY_ST_HCB_APCD_DQ_CLM_FILE_GID),0) AS MAX_NY_ST_HCB_APCD_DQ_CLM_FILE_GID FROM $$DB_STG.V_NY_ST_HCB_APCD_DQ_CLM_FILE ) MAX_GID
    WHERE REC_SEQ = '0800'
    AND CLAIM_TYP LIKE '%PROF%' 
    """,

    """INSERT INTO Sales.SummaryReport (CustomerID, ProductID, TotalQuantity, SaleDate)
            SELECT CustomerID, ProductID, Quantity, SaleDate
            FROM Sales.JanuarySales
            WHERE Region = 'North'
            UNION ALL
            SELECT CustomerID, ProductID, Quantity, SaleDate
            FROM Sales.FebruarySales
            WHERE Region = 'North'
            UNION ALL
            SELECT CustomerID, ProductID, Quantity, SaleDate
            FROM Sales.MarchSales
            WHERE Region = 'North';""",

    """
    INSERT INTO PRJ_INTL_DB_WORK.MPMF_SAP_CUST_EXTNSN_HSTRY
    (
        KUNNR, BUSN_FRMT_CDV, BUSN_FRMT_NM, BUSN_SGMNT_CDV, BUSN_SGMNT_NM, BUSN_SUB_SGMNT_CDV, BUSN_SUB_SGMNT_NM, CLLCTN_TYP_CDV, CLLCTN_TYP_NM, CLSTR_CDV, CLSTR_NM, CUST_INVC_NM, CUST_STOR_SIZE_CDV, CUST_STOR_SIZE_NM, CUST_TEAM_CDV, CUST_TEAM_NM, CUST_TYP_CDV, CUST_TYP_NM, DIVSN_CDV, DIVSN_NM, DSTRCT_CDV, DSTRCT_NM, HRCHY_SLS_CHN_ID, HRCHY_SLS_GRP_ID, OCC_CUST_STTS_CDV, OCC_CUST_STTS_NM, OMEGA_CUST_STTS_CDV, OMEGA_CUST_STTS_NM, OMEGA_INCTVTN_DT, PAYR_KUNNR, PEPSI_CNTCT_NM, PRGRM_CDV, PRGRM_NM, RGN_CDV, RGN_NM, SLOUT_CHN_GRP_ID, SLOUT_FRMT_NM, SLOUT_RGN_ID, SLOUT_SLS_COORDR_ID, SLSMN_RTE_ID, STICC_CUST_STTS_CDV, STICC_CUST_STTS_NM, STOR_NM, TRD_CHNL_CDV, TRD_CHNL_NM, SYS_LAST_MODIFIED_DATE, DW_SYS_ID, DW_BTCH_ID, DW_STEP_ID, DW_CRTD_DTM, DW_UPDT_DTM
    )
    SELECT  
        KUNNR, BUSN_FRMT_CDV, BUSN_FRMT_NM, BUSN_SGMNT_CDV, BUSN_SGMNT_NM, BUSN_SUB_SGMNT_CDV, BUSN_SUB_SGMNT_NM, CLLCTN_TYP_CDV, CLLCTN_TYP_NM, CLSTR_CDV, CLSTR_NM, CUST_INVC_NM, CUST_STOR_SIZE_CDV, CUST_STOR_SIZE_NM, CUST_TEAM_CDV, CUST_TEAM_NM, CUST_TYP_CDV, CUST_TYP_NM, DIVSN_CDV, DIVSN_NM, DSTRCT_CDV, DSTRCT_NM, HRCHY_SLS_CHN_ID, HRCHY_SLS_GRP_ID, OCC_CUST_STTS_CDV, OCC_CUST_STTS_NM, OMEGA_CUST_STTS_CDV, OMEGA_CUST_STTS_NM, OMEGA_INCTVTN_DT, PAYR_KUNNR, PEPSI_CNTCT_NM, PRGRM_CDV, PRGRM_NM, RGN_CDV, RGN_NM, SLOUT_CHN_GRP_ID, SLOUT_FRMT_NM, SLOUT_RGN_ID, SLOUT_SLS_COORDR_ID, SLSMN_RTE_ID, STICC_CUST_STTS_CDV, STICC_CUST_STTS_NM, STOR_NM, TRD_CHNL_CDV, TRD_CHNL_NM, SYS_LAST_MODIFIED_DATE, 371, DW_BTCH_ID, DW_STEP_ID, CURRENT_TIMESTAMP(0), CURRENT_TIMESTAMP(0)
    FROM SAP_CUST_EXTNSN;
    """,
    """
    INSERT INTO Analytics.ReportData
    SELECT 
        a.UserGroup,
        a.UserID,
        b.TransactionDate,
        c.SessionEnd,
        b.CustomerID,
        substr(upper(trim(concat(a.MonthData, ' ', b.TransactionDate))), 1, 50) AS SegmentInfo,
        'Campaign Alpha' AS Campaign
    FROM Marketing.UserSegments AS a
    INNER JOIN Sales.TransactionLogs AS b
    ON a.CustomerID = b.CustomerID
    LEFT OUTER JOIN Analytics.SessionLogs AS c
    ON a.CustomerID = c.CustomerID 
    AND b.TransactionDate >= a.StartDate 
    AND b.TransactionDate <= a.EndDate
    AND b.TransactionDate <= c.SessionEnd;
    """,
    """
    INSERT INTO Finance.BillingData
    SELECT 
        x.Region,
        x.AccountID,
        y.PaymentStart,
        z.PaymentEnd,
        y.ClientID,
        substr(x.Quarter, 1, 100) AS QuarterData,
        'Beta Promo' AS Campaign
    FROM Operations.Accounts AS x
    INNER JOIN Finance.Payments AS y
    ON x.ClientID = y.ClientID
    LEFT OUTER JOIN Finance.PaymentSchedules AS z
    ON y.ClientID = z.ClientID 
    AND y.PaymentStart >= x.StartPeriod 
    AND y.PaymentStart <= x.EndPeriod
    AND y.PaymentStart <= z.PaymentEnd
    INNER JOIN Finance.ClientDetails AS w
    ON y.ClientID = w.ClientID;
    """,
    """
    INSERT INTO HR.EmployeeRecords
    SELECT 
        e.Department,
        e.EmployeeID,
        f.JoinDate,
        g.LeaveDate,
        f.PersonalID,
        substr(e.FiscalYear, 1, 70) AS YearData,
        'Recruitment Drive' AS Campaign
    FROM PeopleManagement.EmployeeData AS e
    INNER JOIN HR.Onboarding AS f
    ON e.PersonalID = f.PersonalID
    LEFT OUTER JOIN HR.LeaveRecords AS g
    ON f.PersonalID = g.PersonalID 
    AND f.JoinDate >= e.StartWindow 
    AND f.JoinDate <= e.EndWindow
    AND f.JoinDate <= g.LeaveDate
    INNER JOIN HR.Performance AS h
    ON f.PersonalID = h.PersonalID
    LEFT OUTER JOIN HR.Benefits AS i
    ON h.PersonalID = i.PersonalID;
    """,
    """
    INSERT INTO Logistics.SupplyData
    SELECT 
        d.LocationGroup,
        d.ItemID,
        h.ShipmentStart,
        i.ShipmentEnd,
        h.SupplierID,
        substr(d.Season, 1, 80) AS SeasonInfo,
        'Distribution Campaign' AS Campaign
    FROM Inventory.ItemRecords AS d
    INNER JOIN Logistics.ShipmentLog AS h
    ON d.SupplierID = h.SupplierID
    LEFT OUTER JOIN Logistics.SupplySchedule AS i
    ON h.SupplierID = i.SupplierID 
    AND h.ShipmentStart >= d.AvailabilityStart 
    AND h.ShipmentStart <= d.AvailabilityEnd
    AND h.ShipmentStart <= i.ShipmentEnd
    INNER JOIN Logistics.SupplierDetails AS j
    ON h.SupplierID = j.SupplierID
    LEFT OUTER JOIN Logistics.ShipmentTracking AS k
    ON j.SupplierID = k.SupplierID
    INNER JOIN Logistics.InventoryStatus AS l
    ON k.SupplierID = l.SupplierID;
    """,
    """
    INSERT INTO Research.DataCollection
    SELECT 
        p.ProjectCategory,
        p.ProjectID,
        r.TestStart,
        s.TestEnd,
        r.ResearcherID,
        substr(p.StudyPhase, 1, 90) AS PhaseData,
        'Analysis Campaign' AS Campaign
    FROM Research.StudyProjects AS p
    INNER JOIN Research.TestRecords AS r
    ON p.ResearcherID = r.ResearcherID
    LEFT OUTER JOIN Research.ResultLogs AS s
    ON r.ResearcherID = s.ResearcherID 
    AND r.TestStart >= p.PlannedStart 
    AND r.TestStart <= p.PlannedEnd
    AND r.TestStart <= s.TestEnd
    INNER JOIN Research.ResearcherDetails AS t
    ON r.ResearcherID = t.ResearcherID
    LEFT OUTER JOIN Research.ProjectFunding AS u
    ON t.ResearcherID = u.ResearcherID
    INNER JOIN Research.LabRecords AS v
    ON u.ResearcherID = v.ResearcherID
    LEFT OUTER JOIN Research.EquipmentLogs AS w
    ON v.ResearcherID = w.ResearcherID;
    """,
    """
    CREATE TABLE PRJ_INTL_DB_WORK.MPMF_SAP_CUST_EXTNSN_HSTRY AS
    SELECT 
        KUNNR, 
        BUSN_FRMT_CDV, 
        BUSN_FRMT_NM, 
        BUSN_SGMNT_CDV, 
        BUSN_SGMNT_NM, 
        BUSN_SUB_SGMNT_CDV, 
        BUSN_SUB_SGMNT_NM, 
        CLLCTN_TYP_CDV, 
        CLLCTN_TYP_NM, 
        CLSTR_CDV, 
        CLSTR_NM, 
        CUST_INVC_NM, 
        CUST_STOR_SIZE_CDV, 
        CUST_STOR_SIZE_NM, 
        CUST_TEAM_CDV, 
        CUST_TEAM_NM, 
        CUST_TYP_CDV, 
        CUST_TYP_NM, 
        DIVSN_CDV, 
        DIVSN_NM, 
        DSTRCT_CDV, 
        DSTRCT_NM, 
        HRCHY_SLS_CHN_ID, 
        HRCHY_SLS_GRP_ID, 
        OCC_CUST_STTS_CDV, 
        OCC_CUST_STTS_NM, 
        OMEGA_CUST_STTS_CDV, 
        OMEGA_CUST_STTS_NM, 
        OMEGA_INCTVTN_DT, 
        PAYR_KUNNR, 
        PEPSI_CNTCT_NM, 
        PRGRM_CDV, 
        PRGRM_NM, 
        RGN_CDV, 
        RGN_NM, 
        SLOUT_CHN_GRP_ID, 
        SLOUT_FRMT_NM, 
        SLOUT_RGN_ID, 
        SLOUT_SLS_COORDR_ID, 
        SLSMN_RTE_ID, 
        STICC_CUST_STTS_CDV, 
        STICC_CUST_STTS_NM, 
        STOR_NM, 
        TRD_CHNL_CDV, 
        TRD_CHNL_NM, 
        SYS_LAST_MODIFIED_DATE, 
        DW_SYS_ID, 
        DW_BTCH_ID, 
        DW_STEP_ID, 
        DW_CRTD_DTM, 
        DW_UPDT_DTM
    FROM SAP_CUST_EXTNSN;
    """
]


queries2 = [
    """INSERT INTO CorpMktg.T2
SELECT
Corporate_Customer_ID,
SiteID,
SiteGroup
FROM CorpMktg.T1;"""
,

    """INSERT INTO CorpMktg.T3019
SELECT
Corporate_Customer_ID,
SiteID
FROM CorpMktg.T2;""",

    """INSERT INTO CorpMktg.T4 (
Corporate_Customer_ID,
SiteID,
SiteGroup
)
SELECT
Corporate_Customer_ID,
SiteID,
SiteGroup
FROM CorpMktg.T3;""",

    """INSERT INTO CorpMktg.T5 (
Corporate_Customer_ID,
SiteID,
SiteGroup
)
SELECT
*
FROM CorpMktg.T4;""",

    """INSERT INTO CorpMktg.T7 (
Trip_Name,
Customer_ID,
Trip_Start_Date,
Trip_End_Date,
Site_Code,
Site_Description,
Promo_Code,
Site_Group,
Campaign_Name,
Phone_No
)
SELECT
CONCAT(a.TripName, ' ', b.TripName) AS Trip_Name,
a.Corporate_Customer_ID AS Customer_ID,
b.TripStart,
c.TripEnd,
CAST(a.SiteID AS VARCHAR(15)) AS Site_Code,
SUBSTR(a.SiteDesc, 1 , 100) AS Site_Description,
TRIM(a.Promo_Cd) AS Promo_Code,
a.SiteGroup AS Site_Group,
'06 - Jan 2024 Group' AS Campaign,
COALESCE(a.ph_no,b.ph_no,'Phone# not available') AS Phone_No
FROM CorpMktg.T5 AS a
INNER JOIN CorpMktg.T6 AS b
ON a.Corporate_Customer_ID = b.Corporate_Customer_ID
LEFT OUTER JOIN CorpMktg.PromotionalTrips_P15 AS c
ON a.Corporate_Customer_ID = c.Corporate_Customer_ID;""",

    """INSERT INTO CorpMktg.T8 (
Sum_Total_Sales,
Avg_Total_Sales,
Min_Total_Sales,
Max_Total_Sales,
Total_Record
)
SELECT SUM(Total_Sales), AVG(Total_Sales), MIN(Total_Sales), MAX(Total_Sales), COUNT(*)
FROM CorpMktg.T7
WHERE Sales_Date >= '2016-01-01';""",

    """INSERT INTO CorpMktg.T10
SELECT
Corporate_Customer_ID,
SiteGroup
FROM CorpMktg.MLNewSeg_Coded_P0;""",

    """INSERT INTO CorpMktg.ML_NewSeg_CodingPrep_NR_P0
SELECT
a.Corporate_Customer_ID,
a.SiteGroup,
b.Departure_Dt,
c.Expected_Start_Dt
FROM CorpMktg.T8 AS a
INNER JOIN CorpMktg.T9 AS b
ON a.Corporate_Customer_ID = b.Corporate_Customer_ID
AND b.Departure_Dt >= a.TripStart
AND b.Departure_Dt <= a.TripEnd
LEFT OUTER JOIN CorpMktg.PromotionalTrips_P0 AS c
ON a.Corporate_Customer_ID = c.Corporate_Customer_ID;""",

    """INSERT INTO CorpMktg.T12
SELECT
a.Corporate_Customer_ID,
a.SiteGroup
FROM CorpMktg.T10 AS a
INNER JOIN CorpMktg.T11 AS b
ON a.Corporate_Customer_ID = b.Corporate_Customer_ID;""",

    """INSERT INTO CorpMktg.T14
SELECT
a.Corporate_Customer_ID,
a.SiteGroup
FROM CorpMktg.T12 AS a
INNER JOIN CorpMktg.T13 AS b
ON a.Corporate_Customer_ID = b.Corporate_Customer_ID;"""
]

queries = queries + queries2
# print(queries)

 
