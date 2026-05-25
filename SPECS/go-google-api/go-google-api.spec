# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           api
%define go_import_path  google.golang.org/api

Name:           go-google-api
Version:        0.280.0
Release:        %autorelease
Summary:        Go module dependency for Prometheus
License:        Apache-2.0
URL:            https://github.com/googleapis/google-api-go-client
#!RemoteAsset:  sha256:bad3e08b3e0da8446e016077facf63927317079c1d5636a0dbe6d3a39b8e2a76
Source0:        https://github.com/googleapis/google-api-go-client/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n google-api-go-client-0.280.0
# google-api imports cloud.google.com/go/auth, while google-cloud-go-auth only
# needs the google.golang.org/api/googleapi leaf package. Keep the leaf package
# in go-google-api-support to break the bootstrap cycle without weakening tests.
# integration-tests/byoid and integration-tests/downscope require Google
# Application Default Credentials, which are not available in OBS.
%define go_test_exclude_glob %{go_import_path}/integration-tests/*
# These tests also require ADC/GCE credentials and fail in OBS with
# GOOGLE_APPLICATION_CREDENTIALS unset or "failed to create creds".
BuildOption(check):  -skip '^(TestNewTokenSource|TestNewClient|TestLogDirectPathMisconfigAttrempDirectPathNotSet|TestLogDirectPathMisconfigNotOnGCE)$'

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(dario.cat/mergo)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cloudflare/circl)
BuildRequires:  go(github.com/cyphar/filepath-securejoin)
BuildRequires:  go(github.com/emirpasic/gods)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-git/gcfg)
BuildRequires:  go(github.com/go-git/go-billy/v5)
BuildRequires:  go(github.com/go-git/go-git/v5)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-github/v59)
BuildRequires:  go(github.com/google/go-querystring)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/googleapis/gax-go/v2/internallog)
BuildRequires:  go(github.com/jbenet/go-context)
BuildRequires:  go(github.com/kevinburke/ssh_config)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/pjbgf/sha1cd)
BuildRequires:  go(github.com/ProtonMail/go-crypto)
BuildRequires:  go(github.com/sergi/go-diff)
BuildRequires:  go(github.com/skeema/knownhosts)
BuildRequires:  go(github.com/xanzy/ssh-agent)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/genproto/googleapis/bytestream)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/warnings.v0)
BuildRequires:  go-rpm-macros

Provides:       go(google.golang.org/api) = %{version}
Provides:       go(google.golang.org/api/abusiveexperiencereport/v1) = %{version}
Provides:       go(google.golang.org/api/acceleratedmobilepageurl/v1) = %{version}
Provides:       go(google.golang.org/api/accessapproval/v1) = %{version}
Provides:       go(google.golang.org/api/accesscontextmanager/v1) = %{version}
Provides:       go(google.golang.org/api/accesscontextmanager/v1beta) = %{version}
Provides:       go(google.golang.org/api/acmedns/v1) = %{version}
Provides:       go(google.golang.org/api/addressvalidation/v1) = %{version}
Provides:       go(google.golang.org/api/adexchangebuyer/v1.2) = %{version}
Provides:       go(google.golang.org/api/adexchangebuyer/v1.3) = %{version}
Provides:       go(google.golang.org/api/adexchangebuyer/v1.4) = %{version}
Provides:       go(google.golang.org/api/adexchangebuyer2/v2beta1) = %{version}
Provides:       go(google.golang.org/api/adexchangeseller/v1) = %{version}
Provides:       go(google.golang.org/api/adexchangeseller/v1.1) = %{version}
Provides:       go(google.golang.org/api/adexchangeseller/v2.0) = %{version}
Provides:       go(google.golang.org/api/adexperiencereport/v1) = %{version}
Provides:       go(google.golang.org/api/admin/datatransfer/v1) = %{version}
Provides:       go(google.golang.org/api/admin/directory/v1) = %{version}
Provides:       go(google.golang.org/api/admin/reports/v1) = %{version}
Provides:       go(google.golang.org/api/admob/v1) = %{version}
Provides:       go(google.golang.org/api/admob/v1beta) = %{version}
Provides:       go(google.golang.org/api/adsense/v1.3) = %{version}
Provides:       go(google.golang.org/api/adsense/v1.4) = %{version}
Provides:       go(google.golang.org/api/adsense/v2) = %{version}
Provides:       go(google.golang.org/api/adsensehost/v4.1) = %{version}
Provides:       go(google.golang.org/api/adsenseplatform/v1) = %{version}
Provides:       go(google.golang.org/api/adsenseplatform/v1alpha) = %{version}
Provides:       go(google.golang.org/api/advisorynotifications/v1) = %{version}
Provides:       go(google.golang.org/api/agentregistry/v1alpha) = %{version}
Provides:       go(google.golang.org/api/aiplatform/v1) = %{version}
Provides:       go(google.golang.org/api/aiplatform/v1beta1) = %{version}
Provides:       go(google.golang.org/api/airquality/v1) = %{version}
Provides:       go(google.golang.org/api/alertcenter/v1beta1) = %{version}
Provides:       go(google.golang.org/api/alloydb/v1) = %{version}
Provides:       go(google.golang.org/api/alloydb/v1alpha) = %{version}
Provides:       go(google.golang.org/api/alloydb/v1beta) = %{version}
Provides:       go(google.golang.org/api/analytics/v2.4) = %{version}
Provides:       go(google.golang.org/api/analytics/v3) = %{version}
Provides:       go(google.golang.org/api/analyticsadmin/v1alpha) = %{version}
Provides:       go(google.golang.org/api/analyticsadmin/v1beta) = %{version}
Provides:       go(google.golang.org/api/analyticsdata/v1alpha) = %{version}
Provides:       go(google.golang.org/api/analyticsdata/v1beta) = %{version}
Provides:       go(google.golang.org/api/analyticshub/v1) = %{version}
Provides:       go(google.golang.org/api/analyticshub/v1beta1) = %{version}
Provides:       go(google.golang.org/api/analyticsreporting/v4) = %{version}
Provides:       go(google.golang.org/api/androiddeviceprovisioning/v1) = %{version}
Provides:       go(google.golang.org/api/androidenterprise/v1) = %{version}
Provides:       go(google.golang.org/api/androidmanagement/v1) = %{version}
Provides:       go(google.golang.org/api/androidpublisher/v1) = %{version}
Provides:       go(google.golang.org/api/androidpublisher/v1.1) = %{version}
Provides:       go(google.golang.org/api/androidpublisher/v2) = %{version}
Provides:       go(google.golang.org/api/androidpublisher/v3) = %{version}
Provides:       go(google.golang.org/api/apigateway/v1) = %{version}
Provides:       go(google.golang.org/api/apigateway/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/apigateway/v1alpha2) = %{version}
Provides:       go(google.golang.org/api/apigateway/v1beta) = %{version}
Provides:       go(google.golang.org/api/apigee/v1) = %{version}
Provides:       go(google.golang.org/api/apigeeregistry/v1) = %{version}
Provides:       go(google.golang.org/api/apihub/v1) = %{version}
Provides:       go(google.golang.org/api/apikeys/v2) = %{version}
Provides:       go(google.golang.org/api/apim/v1alpha) = %{version}
Provides:       go(google.golang.org/api/appengine/v1) = %{version}
Provides:       go(google.golang.org/api/appengine/v1alpha) = %{version}
Provides:       go(google.golang.org/api/appengine/v1beta) = %{version}
Provides:       go(google.golang.org/api/appengine/v1beta4) = %{version}
Provides:       go(google.golang.org/api/appengine/v1beta5) = %{version}
Provides:       go(google.golang.org/api/apphub/v1) = %{version}
Provides:       go(google.golang.org/api/apphub/v1alpha) = %{version}
Provides:       go(google.golang.org/api/appsactivity/v1) = %{version}
Provides:       go(google.golang.org/api/appsmarket/v2) = %{version}
Provides:       go(google.golang.org/api/appstate/v1) = %{version}
Provides:       go(google.golang.org/api/area120tables/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/areainsights/v1) = %{version}
Provides:       go(google.golang.org/api/artifactregistry/v1) = %{version}
Provides:       go(google.golang.org/api/artifactregistry/v1beta1) = %{version}
Provides:       go(google.golang.org/api/artifactregistry/v1beta2) = %{version}
Provides:       go(google.golang.org/api/assuredworkloads/v1) = %{version}
Provides:       go(google.golang.org/api/assuredworkloads/v1beta1) = %{version}
Provides:       go(google.golang.org/api/authorizedbuyersmarketplace/v1) = %{version}
Provides:       go(google.golang.org/api/authorizedbuyersmarketplace/v1alpha) = %{version}
Provides:       go(google.golang.org/api/authorizedbuyersmarketplace/v1beta) = %{version}
Provides:       go(google.golang.org/api/backupdr/v1) = %{version}
Provides:       go(google.golang.org/api/baremetalsolution/v1) = %{version}
Provides:       go(google.golang.org/api/baremetalsolution/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/baremetalsolution/v2) = %{version}
Provides:       go(google.golang.org/api/batch/v1) = %{version}
Provides:       go(google.golang.org/api/beyondcorp/v1) = %{version}
Provides:       go(google.golang.org/api/beyondcorp/v1alpha) = %{version}
Provides:       go(google.golang.org/api/biglake/v1) = %{version}
Provides:       go(google.golang.org/api/bigquery/v2) = %{version}
Provides:       go(google.golang.org/api/bigqueryconnection/v1) = %{version}
Provides:       go(google.golang.org/api/bigqueryconnection/v1beta1) = %{version}
Provides:       go(google.golang.org/api/bigquerydatapolicy/v1) = %{version}
Provides:       go(google.golang.org/api/bigquerydatapolicy/v2) = %{version}
Provides:       go(google.golang.org/api/bigquerydatatransfer/v1) = %{version}
Provides:       go(google.golang.org/api/bigqueryreservation/v1) = %{version}
Provides:       go(google.golang.org/api/bigqueryreservation/v1alpha2) = %{version}
Provides:       go(google.golang.org/api/bigqueryreservation/v1beta1) = %{version}
Provides:       go(google.golang.org/api/bigtableadmin/v1) = %{version}
Provides:       go(google.golang.org/api/bigtableadmin/v2) = %{version}
Provides:       go(google.golang.org/api/billingbudgets/v1) = %{version}
Provides:       go(google.golang.org/api/billingbudgets/v1beta1) = %{version}
Provides:       go(google.golang.org/api/binaryauthorization/v1) = %{version}
Provides:       go(google.golang.org/api/binaryauthorization/v1beta1) = %{version}
Provides:       go(google.golang.org/api/blockchainnodeengine/v1) = %{version}
Provides:       go(google.golang.org/api/blogger/v2) = %{version}
Provides:       go(google.golang.org/api/blogger/v3) = %{version}
Provides:       go(google.golang.org/api/books/v1) = %{version}
Provides:       go(google.golang.org/api/businessprofileperformance/v1) = %{version}
Provides:       go(google.golang.org/api/calendar/v3) = %{version}
Provides:       go(google.golang.org/api/certificatemanager/v1) = %{version}
Provides:       go(google.golang.org/api/ces/v1) = %{version}
Provides:       go(google.golang.org/api/ces/v1beta) = %{version}
Provides:       go(google.golang.org/api/chat/v1) = %{version}
Provides:       go(google.golang.org/api/checks/v1alpha) = %{version}
Provides:       go(google.golang.org/api/chromemanagement/v1) = %{version}
Provides:       go(google.golang.org/api/chromepolicy/v1) = %{version}
Provides:       go(google.golang.org/api/chromeuxreport/v1) = %{version}
Provides:       go(google.golang.org/api/chromewebstore/v1.1) = %{version}
Provides:       go(google.golang.org/api/chromewebstore/v2) = %{version}
Provides:       go(google.golang.org/api/civicinfo/v2) = %{version}
Provides:       go(google.golang.org/api/classroom/v1) = %{version}
Provides:       go(google.golang.org/api/cloudasset/v1) = %{version}
Provides:       go(google.golang.org/api/cloudasset/v1beta1) = %{version}
Provides:       go(google.golang.org/api/cloudasset/v1p1beta1) = %{version}
Provides:       go(google.golang.org/api/cloudasset/v1p4beta1) = %{version}
Provides:       go(google.golang.org/api/cloudasset/v1p5beta1) = %{version}
Provides:       go(google.golang.org/api/cloudasset/v1p7beta1) = %{version}
Provides:       go(google.golang.org/api/cloudbilling/v1) = %{version}
Provides:       go(google.golang.org/api/cloudbilling/v1beta) = %{version}
Provides:       go(google.golang.org/api/cloudbuild/v1) = %{version}
Provides:       go(google.golang.org/api/cloudbuild/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/cloudbuild/v1alpha2) = %{version}
Provides:       go(google.golang.org/api/cloudbuild/v1beta1) = %{version}
Provides:       go(google.golang.org/api/cloudbuild/v2) = %{version}
Provides:       go(google.golang.org/api/cloudchannel/v1) = %{version}
Provides:       go(google.golang.org/api/cloudcommerceprocurement/v1) = %{version}
Provides:       go(google.golang.org/api/cloudcontrolspartner/v1) = %{version}
Provides:       go(google.golang.org/api/cloudcontrolspartner/v1beta) = %{version}
Provides:       go(google.golang.org/api/clouddebugger/v2) = %{version}
Provides:       go(google.golang.org/api/clouddeploy/v1) = %{version}
Provides:       go(google.golang.org/api/clouderrorreporting/v1beta1) = %{version}
Provides:       go(google.golang.org/api/cloudfunctions/v1) = %{version}
Provides:       go(google.golang.org/api/cloudfunctions/v1beta2) = %{version}
Provides:       go(google.golang.org/api/cloudfunctions/v2) = %{version}
Provides:       go(google.golang.org/api/cloudfunctions/v2alpha) = %{version}
Provides:       go(google.golang.org/api/cloudfunctions/v2beta) = %{version}
Provides:       go(google.golang.org/api/cloudidentity/v1) = %{version}
Provides:       go(google.golang.org/api/cloudidentity/v1beta1) = %{version}
Provides:       go(google.golang.org/api/cloudiot/v1) = %{version}
Provides:       go(google.golang.org/api/cloudkms/v1) = %{version}
Provides:       go(google.golang.org/api/cloudlocationfinder/v1) = %{version}
Provides:       go(google.golang.org/api/cloudlocationfinder/v1alpha) = %{version}
Provides:       go(google.golang.org/api/cloudnumberregistry/v1alpha) = %{version}
Provides:       go(google.golang.org/api/cloudprivatecatalog/v1beta1) = %{version}
Provides:       go(google.golang.org/api/cloudprivatecatalogproducer/v1beta1) = %{version}
Provides:       go(google.golang.org/api/cloudprofiler/v2) = %{version}
Provides:       go(google.golang.org/api/cloudresourcemanager/v1) = %{version}
Provides:       go(google.golang.org/api/cloudresourcemanager/v1beta1) = %{version}
Provides:       go(google.golang.org/api/cloudresourcemanager/v2) = %{version}
Provides:       go(google.golang.org/api/cloudresourcemanager/v2beta1) = %{version}
Provides:       go(google.golang.org/api/cloudresourcemanager/v3) = %{version}
Provides:       go(google.golang.org/api/cloudscheduler/v1) = %{version}
Provides:       go(google.golang.org/api/cloudscheduler/v1beta1) = %{version}
Provides:       go(google.golang.org/api/cloudsearch/v1) = %{version}
Provides:       go(google.golang.org/api/cloudshell/v1) = %{version}
Provides:       go(google.golang.org/api/cloudshell/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/cloudsupport/v2) = %{version}
Provides:       go(google.golang.org/api/cloudsupport/v2beta) = %{version}
Provides:       go(google.golang.org/api/cloudtasks/v2) = %{version}
Provides:       go(google.golang.org/api/cloudtasks/v2beta2) = %{version}
Provides:       go(google.golang.org/api/cloudtasks/v2beta3) = %{version}
Provides:       go(google.golang.org/api/cloudtrace/v1) = %{version}
Provides:       go(google.golang.org/api/cloudtrace/v2) = %{version}
Provides:       go(google.golang.org/api/cloudtrace/v2beta1) = %{version}
Provides:       go(google.golang.org/api/commentanalyzer/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/composer/v1) = %{version}
Provides:       go(google.golang.org/api/composer/v1beta1) = %{version}
Provides:       go(google.golang.org/api/compute/v0.alpha) = %{version}
Provides:       go(google.golang.org/api/compute/v0.beta) = %{version}
Provides:       go(google.golang.org/api/compute/v1) = %{version}
Provides:       go(google.golang.org/api/config/v1) = %{version}
Provides:       go(google.golang.org/api/connectors/v1) = %{version}
Provides:       go(google.golang.org/api/connectors/v2) = %{version}
Provides:       go(google.golang.org/api/consumersurveys/v2) = %{version}
Provides:       go(google.golang.org/api/contactcenteraiplatform/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/contactcenterinsights/v1) = %{version}
Provides:       go(google.golang.org/api/container/v1) = %{version}
Provides:       go(google.golang.org/api/container/v1beta1) = %{version}
Provides:       go(google.golang.org/api/containeranalysis/v1) = %{version}
Provides:       go(google.golang.org/api/containeranalysis/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/containeranalysis/v1beta1) = %{version}
Provides:       go(google.golang.org/api/content/v2) = %{version}
Provides:       go(google.golang.org/api/content/v2.1) = %{version}
Provides:       go(google.golang.org/api/content/v2sandbox) = %{version}
Provides:       go(google.golang.org/api/contentwarehouse/v1) = %{version}
Provides:       go(google.golang.org/api/css/v1) = %{version}
Provides:       go(google.golang.org/api/customsearch/v1) = %{version}
Provides:       go(google.golang.org/api/datacatalog/v1) = %{version}
Provides:       go(google.golang.org/api/datacatalog/v1beta1) = %{version}
Provides:       go(google.golang.org/api/dataflow/v1b3) = %{version}
Provides:       go(google.golang.org/api/dataform/v1) = %{version}
Provides:       go(google.golang.org/api/dataform/v1beta1) = %{version}
Provides:       go(google.golang.org/api/datafusion/v1) = %{version}
Provides:       go(google.golang.org/api/datafusion/v1beta1) = %{version}
Provides:       go(google.golang.org/api/datalabeling/v1beta1) = %{version}
Provides:       go(google.golang.org/api/datalineage/v1) = %{version}
Provides:       go(google.golang.org/api/datamanager/v1) = %{version}
Provides:       go(google.golang.org/api/datamigration/v1) = %{version}
Provides:       go(google.golang.org/api/datamigration/v1beta1) = %{version}
Provides:       go(google.golang.org/api/datapipelines/v1) = %{version}
Provides:       go(google.golang.org/api/dataplex/v1) = %{version}
Provides:       go(google.golang.org/api/dataportability/v1) = %{version}
Provides:       go(google.golang.org/api/dataportability/v1beta) = %{version}
Provides:       go(google.golang.org/api/dataproc/v1) = %{version}
Provides:       go(google.golang.org/api/dataproc/v1beta2) = %{version}
Provides:       go(google.golang.org/api/datastore/v1) = %{version}
Provides:       go(google.golang.org/api/datastore/v1beta1) = %{version}
Provides:       go(google.golang.org/api/datastore/v1beta3) = %{version}
Provides:       go(google.golang.org/api/datastream/v1) = %{version}
Provides:       go(google.golang.org/api/datastream/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/deploymentmanager/v0.alpha) = %{version}
Provides:       go(google.golang.org/api/deploymentmanager/v2) = %{version}
Provides:       go(google.golang.org/api/deploymentmanager/v2beta) = %{version}
Provides:       go(google.golang.org/api/developerconnect/v1) = %{version}
Provides:       go(google.golang.org/api/developerknowledge/v1) = %{version}
Provides:       go(google.golang.org/api/developerknowledge/v1alpha) = %{version}
Provides:       go(google.golang.org/api/dfareporting/v2.7) = %{version}
Provides:       go(google.golang.org/api/dfareporting/v3.0) = %{version}
Provides:       go(google.golang.org/api/dfareporting/v3.1) = %{version}
Provides:       go(google.golang.org/api/dfareporting/v3.2) = %{version}
Provides:       go(google.golang.org/api/dfareporting/v3.3) = %{version}
Provides:       go(google.golang.org/api/dfareporting/v3.4) = %{version}
Provides:       go(google.golang.org/api/dfareporting/v3.5) = %{version}
Provides:       go(google.golang.org/api/dfareporting/v4) = %{version}
Provides:       go(google.golang.org/api/dfareporting/v5) = %{version}
Provides:       go(google.golang.org/api/dialogflow/v2) = %{version}
Provides:       go(google.golang.org/api/dialogflow/v2beta1) = %{version}
Provides:       go(google.golang.org/api/dialogflow/v3) = %{version}
Provides:       go(google.golang.org/api/dialogflow/v3alpha1) = %{version}
Provides:       go(google.golang.org/api/dialogflow/v3beta1) = %{version}
Provides:       go(google.golang.org/api/digitalassetlinks/v1) = %{version}
Provides:       go(google.golang.org/api/discovery/v1) = %{version}
Provides:       go(google.golang.org/api/discoveryengine/v1) = %{version}
Provides:       go(google.golang.org/api/discoveryengine/v1alpha) = %{version}
Provides:       go(google.golang.org/api/discoveryengine/v1beta) = %{version}
Provides:       go(google.golang.org/api/displayvideo/v1) = %{version}
Provides:       go(google.golang.org/api/displayvideo/v1beta) = %{version}
Provides:       go(google.golang.org/api/displayvideo/v1beta2) = %{version}
Provides:       go(google.golang.org/api/displayvideo/v1dev) = %{version}
Provides:       go(google.golang.org/api/displayvideo/v2) = %{version}
Provides:       go(google.golang.org/api/displayvideo/v3) = %{version}
Provides:       go(google.golang.org/api/displayvideo/v4) = %{version}
Provides:       go(google.golang.org/api/dlp/v2) = %{version}
Provides:       go(google.golang.org/api/dns/v1) = %{version}
Provides:       go(google.golang.org/api/dns/v1beta2) = %{version}
Provides:       go(google.golang.org/api/dns/v2) = %{version}
Provides:       go(google.golang.org/api/dns/v2beta1) = %{version}
Provides:       go(google.golang.org/api/docs/v1) = %{version}
Provides:       go(google.golang.org/api/documentai/v1) = %{version}
Provides:       go(google.golang.org/api/documentai/v1beta2) = %{version}
Provides:       go(google.golang.org/api/documentai/v1beta3) = %{version}
Provides:       go(google.golang.org/api/domains/v1) = %{version}
Provides:       go(google.golang.org/api/domains/v1alpha2) = %{version}
Provides:       go(google.golang.org/api/domains/v1beta1) = %{version}
Provides:       go(google.golang.org/api/domainsrdap/v1) = %{version}
Provides:       go(google.golang.org/api/doubleclickbidmanager/v1) = %{version}
Provides:       go(google.golang.org/api/doubleclickbidmanager/v1.1) = %{version}
Provides:       go(google.golang.org/api/doubleclickbidmanager/v2) = %{version}
Provides:       go(google.golang.org/api/doubleclicksearch/v2) = %{version}
Provides:       go(google.golang.org/api/drive/v2) = %{version}
Provides:       go(google.golang.org/api/drive/v3) = %{version}
Provides:       go(google.golang.org/api/driveactivity/v2) = %{version}
Provides:       go(google.golang.org/api/drivelabels/v2) = %{version}
Provides:       go(google.golang.org/api/drivelabels/v2beta) = %{version}
Provides:       go(google.golang.org/api/essentialcontacts/v1) = %{version}
Provides:       go(google.golang.org/api/eventarc/v1) = %{version}
Provides:       go(google.golang.org/api/eventarc/v1beta1) = %{version}
Provides:       go(google.golang.org/api/factchecktools/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/fcm/v1) = %{version}
Provides:       go(google.golang.org/api/fcmdata/v1beta1) = %{version}
Provides:       go(google.golang.org/api/file/v1) = %{version}
Provides:       go(google.golang.org/api/file/v1beta1) = %{version}
Provides:       go(google.golang.org/api/firebase/v1beta1) = %{version}
Provides:       go(google.golang.org/api/firebaseappcheck/v1) = %{version}
Provides:       go(google.golang.org/api/firebaseappcheck/v1beta) = %{version}
Provides:       go(google.golang.org/api/firebaseappdistribution/v1) = %{version}
Provides:       go(google.golang.org/api/firebaseappdistribution/v1alpha) = %{version}
Provides:       go(google.golang.org/api/firebaseapphosting/v1) = %{version}
Provides:       go(google.golang.org/api/firebaseapphosting/v1beta) = %{version}
Provides:       go(google.golang.org/api/firebasedatabase/v1beta) = %{version}
Provides:       go(google.golang.org/api/firebasedataconnect/v1) = %{version}
Provides:       go(google.golang.org/api/firebasedataconnect/v1beta) = %{version}
Provides:       go(google.golang.org/api/firebasedynamiclinks/v1) = %{version}
Provides:       go(google.golang.org/api/firebasehosting/v1) = %{version}
Provides:       go(google.golang.org/api/firebasehosting/v1beta1) = %{version}
Provides:       go(google.golang.org/api/firebaseml/v1) = %{version}
Provides:       go(google.golang.org/api/firebaseml/v1beta2) = %{version}
Provides:       go(google.golang.org/api/firebaseml/v2beta) = %{version}
Provides:       go(google.golang.org/api/firebaserules/v1) = %{version}
Provides:       go(google.golang.org/api/firebasestorage/v1beta) = %{version}
Provides:       go(google.golang.org/api/firestore/v1) = %{version}
Provides:       go(google.golang.org/api/firestore/v1beta1) = %{version}
Provides:       go(google.golang.org/api/firestore/v1beta2) = %{version}
Provides:       go(google.golang.org/api/fitness/v1) = %{version}
Provides:       go(google.golang.org/api/forms/v1) = %{version}
Provides:       go(google.golang.org/api/fusiontables/v1) = %{version}
Provides:       go(google.golang.org/api/fusiontables/v2) = %{version}
Provides:       go(google.golang.org/api/games/v1) = %{version}
Provides:       go(google.golang.org/api/gamesconfiguration/v1configuration) = %{version}
Provides:       go(google.golang.org/api/gameservices/v1) = %{version}
Provides:       go(google.golang.org/api/gameservices/v1beta) = %{version}
Provides:       go(google.golang.org/api/gamesmanagement/v1management) = %{version}
Provides:       go(google.golang.org/api/genomics/v1) = %{version}
Provides:       go(google.golang.org/api/genomics/v1alpha2) = %{version}
Provides:       go(google.golang.org/api/genomics/v2alpha1) = %{version}
Provides:       go(google.golang.org/api/gkebackup/v1) = %{version}
Provides:       go(google.golang.org/api/gkehub/v1) = %{version}
Provides:       go(google.golang.org/api/gkehub/v1alpha) = %{version}
Provides:       go(google.golang.org/api/gkehub/v1alpha2) = %{version}
Provides:       go(google.golang.org/api/gkehub/v1beta) = %{version}
Provides:       go(google.golang.org/api/gkehub/v1beta1) = %{version}
Provides:       go(google.golang.org/api/gkehub/v2) = %{version}
Provides:       go(google.golang.org/api/gkehub/v2alpha) = %{version}
Provides:       go(google.golang.org/api/gkehub/v2beta) = %{version}
Provides:       go(google.golang.org/api/gkeonprem/v1) = %{version}
Provides:       go(google.golang.org/api/gmail/v1) = %{version}
Provides:       go(google.golang.org/api/gmailpostmastertools/v1) = %{version}
Provides:       go(google.golang.org/api/gmailpostmastertools/v1beta1) = %{version}
Provides:       go(google.golang.org/api/gmailpostmastertools/v2) = %{version}
Provides:       go(google.golang.org/api/google-api-go-generator/internal/disco) = %{version}
Provides:       go(google.golang.org/api/groupsmigration/v1) = %{version}
Provides:       go(google.golang.org/api/groupssettings/v1) = %{version}
Provides:       go(google.golang.org/api/health/v4) = %{version}
Provides:       go(google.golang.org/api/healthcare/v1) = %{version}
Provides:       go(google.golang.org/api/healthcare/v1alpha) = %{version}
Provides:       go(google.golang.org/api/healthcare/v1alpha2) = %{version}
Provides:       go(google.golang.org/api/healthcare/v1beta1) = %{version}
Provides:       go(google.golang.org/api/homegraph/v1) = %{version}
Provides:       go(google.golang.org/api/hypercomputecluster/v1) = %{version}
Provides:       go(google.golang.org/api/iam/v1) = %{version}
Provides:       go(google.golang.org/api/iam/v2) = %{version}
Provides:       go(google.golang.org/api/iam/v2beta) = %{version}
Provides:       go(google.golang.org/api/iamcredentials/v1) = %{version}
Provides:       go(google.golang.org/api/iap/v1) = %{version}
Provides:       go(google.golang.org/api/iap/v1beta1) = %{version}
Provides:       go(google.golang.org/api/ideahub/v1alpha) = %{version}
Provides:       go(google.golang.org/api/ideahub/v1beta) = %{version}
Provides:       go(google.golang.org/api/identitytoolkit/v1) = %{version}
Provides:       go(google.golang.org/api/identitytoolkit/v2) = %{version}
Provides:       go(google.golang.org/api/identitytoolkit/v3) = %{version}
Provides:       go(google.golang.org/api/ids/v1) = %{version}
Provides:       go(google.golang.org/api/idtoken) = %{version}
Provides:       go(google.golang.org/api/impersonate) = %{version}
Provides:       go(google.golang.org/api/indexing/v3) = %{version}
Provides:       go(google.golang.org/api/integration-tests/byoid) = %{version}
Provides:       go(google.golang.org/api/integration-tests/downscope) = %{version}
Provides:       go(google.golang.org/api/integrations/v1) = %{version}
Provides:       go(google.golang.org/api/integrations/v1alpha) = %{version}
Provides:       go(google.golang.org/api/internal) = %{version}
Provides:       go(google.golang.org/api/internal/cert) = %{version}
Provides:       go(google.golang.org/api/internal/credentialstype) = %{version}
Provides:       go(google.golang.org/api/internal/gensupport) = %{version}
Provides:       go(google.golang.org/api/internal/impersonate) = %{version}
Provides:       go(google.golang.org/api/jobs/v2) = %{version}
Provides:       go(google.golang.org/api/jobs/v3) = %{version}
Provides:       go(google.golang.org/api/jobs/v3p1beta1) = %{version}
Provides:       go(google.golang.org/api/jobs/v4) = %{version}
Provides:       go(google.golang.org/api/keep/v1) = %{version}
Provides:       go(google.golang.org/api/kgsearch/v1) = %{version}
Provides:       go(google.golang.org/api/kmsinventory/v1) = %{version}
Provides:       go(google.golang.org/api/language/v1) = %{version}
Provides:       go(google.golang.org/api/language/v1beta1) = %{version}
Provides:       go(google.golang.org/api/language/v1beta2) = %{version}
Provides:       go(google.golang.org/api/language/v2) = %{version}
Provides:       go(google.golang.org/api/libraryagent/v1) = %{version}
Provides:       go(google.golang.org/api/licensing/v1) = %{version}
Provides:       go(google.golang.org/api/lifesciences/v2beta) = %{version}
Provides:       go(google.golang.org/api/localservices/v1) = %{version}
Provides:       go(google.golang.org/api/logging/v2) = %{version}
Provides:       go(google.golang.org/api/logging/v2beta1) = %{version}
Provides:       go(google.golang.org/api/looker/v1) = %{version}
Provides:       go(google.golang.org/api/managedidentities/v1) = %{version}
Provides:       go(google.golang.org/api/managedidentities/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/managedidentities/v1beta1) = %{version}
Provides:       go(google.golang.org/api/managedkafka/v1) = %{version}
Provides:       go(google.golang.org/api/manufacturers/v1) = %{version}
Provides:       go(google.golang.org/api/marketingplatformadmin/v1alpha) = %{version}
Provides:       go(google.golang.org/api/meet/v2) = %{version}
Provides:       go(google.golang.org/api/memcache/v1) = %{version}
Provides:       go(google.golang.org/api/memcache/v1beta2) = %{version}
Provides:       go(google.golang.org/api/merchantapi/accounts/v1) = %{version}
Provides:       go(google.golang.org/api/merchantapi/accounts_v1beta) = %{version}
Provides:       go(google.golang.org/api/merchantapi/conversions/v1) = %{version}
Provides:       go(google.golang.org/api/merchantapi/conversions_v1beta) = %{version}
Provides:       go(google.golang.org/api/merchantapi/datasources/v1) = %{version}
Provides:       go(google.golang.org/api/merchantapi/datasources_v1beta) = %{version}
Provides:       go(google.golang.org/api/merchantapi/inventories/v1) = %{version}
Provides:       go(google.golang.org/api/merchantapi/inventories_v1beta) = %{version}
Provides:       go(google.golang.org/api/merchantapi/issueresolution/v1) = %{version}
Provides:       go(google.golang.org/api/merchantapi/issueresolution_v1beta) = %{version}
Provides:       go(google.golang.org/api/merchantapi/lfp/v1) = %{version}
Provides:       go(google.golang.org/api/merchantapi/lfp_v1beta) = %{version}
Provides:       go(google.golang.org/api/merchantapi/notifications/v1) = %{version}
Provides:       go(google.golang.org/api/merchantapi/notifications_v1beta) = %{version}
Provides:       go(google.golang.org/api/merchantapi/ordertracking/v1) = %{version}
Provides:       go(google.golang.org/api/merchantapi/ordertracking_v1beta) = %{version}
Provides:       go(google.golang.org/api/merchantapi/products/v1) = %{version}
Provides:       go(google.golang.org/api/merchantapi/products_v1beta) = %{version}
Provides:       go(google.golang.org/api/merchantapi/promotions/v1) = %{version}
Provides:       go(google.golang.org/api/merchantapi/promotions_v1beta) = %{version}
Provides:       go(google.golang.org/api/merchantapi/quota/v1) = %{version}
Provides:       go(google.golang.org/api/merchantapi/quota_v1beta) = %{version}
Provides:       go(google.golang.org/api/merchantapi/reports/v1) = %{version}
Provides:       go(google.golang.org/api/merchantapi/reports_v1beta) = %{version}
Provides:       go(google.golang.org/api/merchantapi/reviews_v1beta) = %{version}
Provides:       go(google.golang.org/api/metastore/v1) = %{version}
Provides:       go(google.golang.org/api/metastore/v1alpha) = %{version}
Provides:       go(google.golang.org/api/metastore/v1beta) = %{version}
Provides:       go(google.golang.org/api/metastore/v2) = %{version}
Provides:       go(google.golang.org/api/metastore/v2alpha) = %{version}
Provides:       go(google.golang.org/api/metastore/v2beta) = %{version}
Provides:       go(google.golang.org/api/migrationcenter/v1) = %{version}
Provides:       go(google.golang.org/api/migrationcenter/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/mirror/v1) = %{version}
Provides:       go(google.golang.org/api/ml/v1) = %{version}
Provides:       go(google.golang.org/api/monitoring/v1) = %{version}
Provides:       go(google.golang.org/api/monitoring/v3) = %{version}
Provides:       go(google.golang.org/api/mybusinessaccountmanagement/v1) = %{version}
Provides:       go(google.golang.org/api/mybusinessbusinesscalls/v1) = %{version}
Provides:       go(google.golang.org/api/mybusinessbusinessinformation/v1) = %{version}
Provides:       go(google.golang.org/api/mybusinesslodging/v1) = %{version}
Provides:       go(google.golang.org/api/mybusinessnotifications/v1) = %{version}
Provides:       go(google.golang.org/api/mybusinessplaceactions/v1) = %{version}
Provides:       go(google.golang.org/api/mybusinessqanda/v1) = %{version}
Provides:       go(google.golang.org/api/mybusinessverifications/v1) = %{version}
Provides:       go(google.golang.org/api/netapp/v1) = %{version}
Provides:       go(google.golang.org/api/netapp/v1beta1) = %{version}
Provides:       go(google.golang.org/api/networkconnectivity/v1) = %{version}
Provides:       go(google.golang.org/api/networkconnectivity/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/networkmanagement/v1) = %{version}
Provides:       go(google.golang.org/api/networkmanagement/v1beta1) = %{version}
Provides:       go(google.golang.org/api/networksecurity/v1) = %{version}
Provides:       go(google.golang.org/api/networksecurity/v1beta1) = %{version}
Provides:       go(google.golang.org/api/networkservices/v1) = %{version}
Provides:       go(google.golang.org/api/networkservices/v1beta1) = %{version}
Provides:       go(google.golang.org/api/notebooks/v1) = %{version}
Provides:       go(google.golang.org/api/notebooks/v2) = %{version}
Provides:       go(google.golang.org/api/oauth2/v1) = %{version}
Provides:       go(google.golang.org/api/oauth2/v2) = %{version}
Provides:       go(google.golang.org/api/observability/v1) = %{version}
Provides:       go(google.golang.org/api/ondemandscanning/v1) = %{version}
Provides:       go(google.golang.org/api/ondemandscanning/v1beta1) = %{version}
Provides:       go(google.golang.org/api/option) = %{version}
Provides:       go(google.golang.org/api/option/internaloption) = %{version}
Provides:       go(google.golang.org/api/oracledatabase/v1) = %{version}
Provides:       go(google.golang.org/api/orgpolicy/v2) = %{version}
Provides:       go(google.golang.org/api/osconfig/v1) = %{version}
Provides:       go(google.golang.org/api/osconfig/v1alpha) = %{version}
Provides:       go(google.golang.org/api/osconfig/v1beta) = %{version}
Provides:       go(google.golang.org/api/osconfig/v2) = %{version}
Provides:       go(google.golang.org/api/osconfig/v2beta) = %{version}
Provides:       go(google.golang.org/api/oslogin/v1) = %{version}
Provides:       go(google.golang.org/api/oslogin/v1alpha) = %{version}
Provides:       go(google.golang.org/api/oslogin/v1beta) = %{version}
Provides:       go(google.golang.org/api/pagespeedonline/v1) = %{version}
Provides:       go(google.golang.org/api/pagespeedonline/v2) = %{version}
Provides:       go(google.golang.org/api/pagespeedonline/v4) = %{version}
Provides:       go(google.golang.org/api/pagespeedonline/v5) = %{version}
Provides:       go(google.golang.org/api/parallelstore/v1) = %{version}
Provides:       go(google.golang.org/api/parallelstore/v1beta) = %{version}
Provides:       go(google.golang.org/api/parametermanager/v1) = %{version}
Provides:       go(google.golang.org/api/partners/v2) = %{version}
Provides:       go(google.golang.org/api/paymentsresellersubscription/v1) = %{version}
Provides:       go(google.golang.org/api/people/v1) = %{version}
Provides:       go(google.golang.org/api/places/v1) = %{version}
Provides:       go(google.golang.org/api/playablelocations/v3) = %{version}
Provides:       go(google.golang.org/api/playcustomapp/v1) = %{version}
Provides:       go(google.golang.org/api/playdeveloperreporting/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/playdeveloperreporting/v1beta1) = %{version}
Provides:       go(google.golang.org/api/playgrouping/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/playintegrity/v1) = %{version}
Provides:       go(google.golang.org/api/playmoviespartner/v1) = %{version}
Provides:       go(google.golang.org/api/plus/v1) = %{version}
Provides:       go(google.golang.org/api/plusdomains/v1) = %{version}
Provides:       go(google.golang.org/api/policyanalyzer/v1) = %{version}
Provides:       go(google.golang.org/api/policyanalyzer/v1beta1) = %{version}
Provides:       go(google.golang.org/api/policysimulator/v1) = %{version}
Provides:       go(google.golang.org/api/policysimulator/v1alpha) = %{version}
Provides:       go(google.golang.org/api/policysimulator/v1beta) = %{version}
Provides:       go(google.golang.org/api/policysimulator/v1beta1) = %{version}
Provides:       go(google.golang.org/api/policytroubleshooter/v1) = %{version}
Provides:       go(google.golang.org/api/policytroubleshooter/v1beta) = %{version}
Provides:       go(google.golang.org/api/policytroubleshooter/v3) = %{version}
Provides:       go(google.golang.org/api/policytroubleshooter/v3beta) = %{version}
Provides:       go(google.golang.org/api/pollen/v1) = %{version}
Provides:       go(google.golang.org/api/poly/v1) = %{version}
Provides:       go(google.golang.org/api/privateca/v1) = %{version}
Provides:       go(google.golang.org/api/privateca/v1beta1) = %{version}
Provides:       go(google.golang.org/api/prod_tt_sasportal/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/proximitybeacon/v1beta1) = %{version}
Provides:       go(google.golang.org/api/publicca/v1) = %{version}
Provides:       go(google.golang.org/api/publicca/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/publicca/v1beta1) = %{version}
Provides:       go(google.golang.org/api/pubsub/v1) = %{version}
Provides:       go(google.golang.org/api/pubsub/v1beta1a) = %{version}
Provides:       go(google.golang.org/api/pubsub/v1beta2) = %{version}
Provides:       go(google.golang.org/api/pubsublite/v1) = %{version}
Provides:       go(google.golang.org/api/qpxexpress/v1) = %{version}
Provides:       go(google.golang.org/api/rapidmigrationassessment/v1) = %{version}
Provides:       go(google.golang.org/api/readerrevenuesubscriptionlinking/v1) = %{version}
Provides:       go(google.golang.org/api/realtimebidding/v1) = %{version}
Provides:       go(google.golang.org/api/realtimebidding/v1alpha) = %{version}
Provides:       go(google.golang.org/api/recaptchaenterprise/v1) = %{version}
Provides:       go(google.golang.org/api/recommendationengine/v1beta1) = %{version}
Provides:       go(google.golang.org/api/recommender/v1) = %{version}
Provides:       go(google.golang.org/api/recommender/v1beta1) = %{version}
Provides:       go(google.golang.org/api/redis/v1) = %{version}
Provides:       go(google.golang.org/api/redis/v1beta1) = %{version}
Provides:       go(google.golang.org/api/remotebuildexecution/v1) = %{version}
Provides:       go(google.golang.org/api/remotebuildexecution/v1alpha) = %{version}
Provides:       go(google.golang.org/api/remotebuildexecution/v2) = %{version}
Provides:       go(google.golang.org/api/replicapool/v1beta1) = %{version}
Provides:       go(google.golang.org/api/replicapoolupdater/v1beta1) = %{version}
Provides:       go(google.golang.org/api/reseller/v1) = %{version}
Provides:       go(google.golang.org/api/resourcesettings/v1) = %{version}
Provides:       go(google.golang.org/api/retail/v2) = %{version}
Provides:       go(google.golang.org/api/retail/v2alpha) = %{version}
Provides:       go(google.golang.org/api/retail/v2beta) = %{version}
Provides:       go(google.golang.org/api/run/v1) = %{version}
Provides:       go(google.golang.org/api/run/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/run/v1beta1) = %{version}
Provides:       go(google.golang.org/api/run/v2) = %{version}
Provides:       go(google.golang.org/api/runtimeconfig/v1) = %{version}
Provides:       go(google.golang.org/api/runtimeconfig/v1beta1) = %{version}
Provides:       go(google.golang.org/api/saasservicemgmt/v1) = %{version}
Provides:       go(google.golang.org/api/saasservicemgmt/v1beta1) = %{version}
Provides:       go(google.golang.org/api/safebrowsing/v4) = %{version}
Provides:       go(google.golang.org/api/safebrowsing/v5) = %{version}
Provides:       go(google.golang.org/api/sasportal/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/script/v1) = %{version}
Provides:       go(google.golang.org/api/searchads360/v0) = %{version}
Provides:       go(google.golang.org/api/searchconsole/v1) = %{version}
Provides:       go(google.golang.org/api/secretmanager/v1) = %{version}
Provides:       go(google.golang.org/api/secretmanager/v1beta1) = %{version}
Provides:       go(google.golang.org/api/secretmanager/v1beta2) = %{version}
Provides:       go(google.golang.org/api/securesourcemanager/v1) = %{version}
Provides:       go(google.golang.org/api/securitycenter/v1) = %{version}
Provides:       go(google.golang.org/api/securitycenter/v1beta1) = %{version}
Provides:       go(google.golang.org/api/securitycenter/v1beta2) = %{version}
Provides:       go(google.golang.org/api/securitycenter/v1p1alpha1) = %{version}
Provides:       go(google.golang.org/api/securitycenter/v1p1beta1) = %{version}
Provides:       go(google.golang.org/api/securityposture/v1) = %{version}
Provides:       go(google.golang.org/api/servicebroker/v1) = %{version}
Provides:       go(google.golang.org/api/servicebroker/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/servicebroker/v1beta1) = %{version}
Provides:       go(google.golang.org/api/serviceconsumermanagement/v1) = %{version}
Provides:       go(google.golang.org/api/serviceconsumermanagement/v1beta1) = %{version}
Provides:       go(google.golang.org/api/servicecontrol/v1) = %{version}
Provides:       go(google.golang.org/api/servicecontrol/v2) = %{version}
Provides:       go(google.golang.org/api/servicedirectory/v1) = %{version}
Provides:       go(google.golang.org/api/servicedirectory/v1beta1) = %{version}
Provides:       go(google.golang.org/api/servicemanagement/v1) = %{version}
Provides:       go(google.golang.org/api/servicenetworking/v1) = %{version}
Provides:       go(google.golang.org/api/servicenetworking/v1beta) = %{version}
Provides:       go(google.golang.org/api/serviceusage/v1) = %{version}
Provides:       go(google.golang.org/api/serviceusage/v1beta1) = %{version}
Provides:       go(google.golang.org/api/serviceuser/v1) = %{version}
Provides:       go(google.golang.org/api/sheets/v4) = %{version}
Provides:       go(google.golang.org/api/siteverification/v1) = %{version}
Provides:       go(google.golang.org/api/slides/v1) = %{version}
Provides:       go(google.golang.org/api/smartdevicemanagement/v1) = %{version}
Provides:       go(google.golang.org/api/solar/v1) = %{version}
Provides:       go(google.golang.org/api/sourcerepo/v1) = %{version}
Provides:       go(google.golang.org/api/spanner/v1) = %{version}
Provides:       go(google.golang.org/api/spectrum/v1explorer) = %{version}
Provides:       go(google.golang.org/api/speech/v1) = %{version}
Provides:       go(google.golang.org/api/speech/v1beta1) = %{version}
Provides:       go(google.golang.org/api/speech/v1p1beta1) = %{version}
Provides:       go(google.golang.org/api/speech/v2beta) = %{version}
Provides:       go(google.golang.org/api/speech/v2beta1) = %{version}
Provides:       go(google.golang.org/api/sql/v1beta4) = %{version}
Provides:       go(google.golang.org/api/sqladmin/v1) = %{version}
Provides:       go(google.golang.org/api/sqladmin/v1beta4) = %{version}
Provides:       go(google.golang.org/api/storage/v1) = %{version}
Provides:       go(google.golang.org/api/storage/v1beta1) = %{version}
Provides:       go(google.golang.org/api/storage/v1beta2) = %{version}
Provides:       go(google.golang.org/api/storagebatchoperations/v1) = %{version}
Provides:       go(google.golang.org/api/storagetransfer/v1) = %{version}
Provides:       go(google.golang.org/api/streetviewpublish/v1) = %{version}
Provides:       go(google.golang.org/api/sts/v1) = %{version}
Provides:       go(google.golang.org/api/sts/v1beta) = %{version}
Provides:       go(google.golang.org/api/support/bundler) = %{version}
Provides:       go(google.golang.org/api/surveys/v2) = %{version}
Provides:       go(google.golang.org/api/tagmanager/v1) = %{version}
Provides:       go(google.golang.org/api/tagmanager/v2) = %{version}
Provides:       go(google.golang.org/api/tasks/v1) = %{version}
Provides:       go(google.golang.org/api/testing/v1) = %{version}
Provides:       go(google.golang.org/api/texttospeech/v1) = %{version}
Provides:       go(google.golang.org/api/texttospeech/v1beta1) = %{version}
Provides:       go(google.golang.org/api/threatintelligence/v1beta) = %{version}
Provides:       go(google.golang.org/api/toolresults/v1) = %{version}
Provides:       go(google.golang.org/api/toolresults/v1beta3) = %{version}
Provides:       go(google.golang.org/api/tpu/v1) = %{version}
Provides:       go(google.golang.org/api/tpu/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/tpu/v2) = %{version}
Provides:       go(google.golang.org/api/tpu/v2alpha1) = %{version}
Provides:       go(google.golang.org/api/tracing/v2) = %{version}
Provides:       go(google.golang.org/api/trafficdirector/v2) = %{version}
Provides:       go(google.golang.org/api/trafficdirector/v3) = %{version}
Provides:       go(google.golang.org/api/transcoder/v1) = %{version}
Provides:       go(google.golang.org/api/transcoder/v1beta1) = %{version}
Provides:       go(google.golang.org/api/translate/v2) = %{version}
Provides:       go(google.golang.org/api/translate/v3) = %{version}
Provides:       go(google.golang.org/api/translate/v3beta1) = %{version}
Provides:       go(google.golang.org/api/transport) = %{version}
Provides:       go(google.golang.org/api/transport/bytestream) = %{version}
Provides:       go(google.golang.org/api/transport/bytestream/internal) = %{version}
Provides:       go(google.golang.org/api/transport/grpc) = %{version}
Provides:       go(google.golang.org/api/transport/http) = %{version}
Provides:       go(google.golang.org/api/travelimpactmodel/v1) = %{version}
Provides:       go(google.golang.org/api/urlshortener/v1) = %{version}
Provides:       go(google.golang.org/api/vault/v1) = %{version}
Provides:       go(google.golang.org/api/vectortile/v1) = %{version}
Provides:       go(google.golang.org/api/verifiedaccess/v1) = %{version}
Provides:       go(google.golang.org/api/verifiedaccess/v2) = %{version}
Provides:       go(google.golang.org/api/versionhistory/v1) = %{version}
Provides:       go(google.golang.org/api/videointelligence/v1) = %{version}
Provides:       go(google.golang.org/api/videointelligence/v1beta2) = %{version}
Provides:       go(google.golang.org/api/videointelligence/v1p1beta1) = %{version}
Provides:       go(google.golang.org/api/videointelligence/v1p2beta1) = %{version}
Provides:       go(google.golang.org/api/videointelligence/v1p3beta1) = %{version}
Provides:       go(google.golang.org/api/vision/v1) = %{version}
Provides:       go(google.golang.org/api/vision/v1p1beta1) = %{version}
Provides:       go(google.golang.org/api/vision/v1p2beta1) = %{version}
Provides:       go(google.golang.org/api/vmmigration/v1) = %{version}
Provides:       go(google.golang.org/api/vmmigration/v1alpha1) = %{version}
Provides:       go(google.golang.org/api/vmwareengine/v1) = %{version}
Provides:       go(google.golang.org/api/vpcaccess/v1) = %{version}
Provides:       go(google.golang.org/api/vpcaccess/v1beta1) = %{version}
Provides:       go(google.golang.org/api/walletobjects/v1) = %{version}
Provides:       go(google.golang.org/api/webfonts/v1) = %{version}
Provides:       go(google.golang.org/api/webmasters/v3) = %{version}
Provides:       go(google.golang.org/api/webrisk/v1) = %{version}
Provides:       go(google.golang.org/api/websecurityscanner/v1) = %{version}
Provides:       go(google.golang.org/api/websecurityscanner/v1alpha) = %{version}
Provides:       go(google.golang.org/api/websecurityscanner/v1beta) = %{version}
Provides:       go(google.golang.org/api/workflowexecutions/v1) = %{version}
Provides:       go(google.golang.org/api/workflowexecutions/v1beta) = %{version}
Provides:       go(google.golang.org/api/workflows/v1) = %{version}
Provides:       go(google.golang.org/api/workflows/v1beta) = %{version}
Provides:       go(google.golang.org/api/workloadmanager/v1) = %{version}
Provides:       go(google.golang.org/api/workspaceevents/v1) = %{version}
Provides:       go(google.golang.org/api/workstations/v1) = %{version}
Provides:       go(google.golang.org/api/workstations/v1beta) = %{version}
Provides:       go(google.golang.org/api/youtube/v3) = %{version}
Provides:       go(google.golang.org/api/youtubeanalytics/v1) = %{version}
Provides:       go(google.golang.org/api/youtubeanalytics/v1beta1) = %{version}
Provides:       go(google.golang.org/api/youtubeanalytics/v2) = %{version}
Provides:       go(google.golang.org/api/youtubereporting/v1) = %{version}

Requires:       go(cloud.google.com/go/auth)
Requires:       go(cloud.google.com/go/auth/oauth2adapt)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(dario.cat/mergo)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/cloudflare/circl)
Requires:       go(github.com/cyphar/filepath-securejoin)
Requires:       go(github.com/emirpasic/gods)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/go-git/gcfg)
Requires:       go(github.com/go-git/go-billy/v5)
Requires:       go(github.com/go-git/go-git/v5)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-github/v59)
Requires:       go(github.com/google/go-querystring)
Requires:       go(github.com/google/s2a-go)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/googleapis/enterprise-certificate-proxy)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(github.com/googleapis/gax-go/v2/internallog)
Requires:       go(github.com/jbenet/go-context)
Requires:       go(github.com/kevinburke/ssh_config)
Requires:       go(github.com/klauspost/cpuid/v2)
Requires:       go(github.com/pjbgf/sha1cd)
Requires:       go(github.com/ProtonMail/go-crypto)
Requires:       go(github.com/sergi/go-diff)
Requires:       go(github.com/skeema/knownhosts)
Requires:       go(github.com/xanzy/ssh-agent)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/api/googleapi)
Requires:       go(google.golang.org/api/internal/third_party/uritemplates)
Requires:       go(google.golang.org/api/iterator)
Requires:       go(google.golang.org/genproto/googleapis/bytestream)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/warnings.v0)

%description
Go module dependency for Prometheus. Generated by go2spec.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/googleapi
%exclude %{go_sys_gopath}/%{go_import_path}/internal/third_party/uritemplates
%exclude %{go_sys_gopath}/%{go_import_path}/iterator

%changelog
%autochangelog
