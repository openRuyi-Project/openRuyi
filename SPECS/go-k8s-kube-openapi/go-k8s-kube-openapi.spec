# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kube-openapi
%define go_import_path  k8s.io/kube-openapi
%define commit_id 43fb72c5454a03ed83388cf20c070499ee359af8
# OBS test logs show optional integration dependencies under test/integration.
# Keep non-integration package checks enabled. - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/test/integration*
}

Name:           go-k8s-kube-openapi
Version:        0+git20260317.43fb72c
Release:        %autorelease
Summary:        Kubernetes OpenAPI discovery spec generation for Go
License:        Apache-2.0
URL:            https://github.com/kubernetes/kube-openapi
#!RemoteAsset:  sha256:e1d1ef775eb190aeef3eccc0e42ebd0eca119ff474c05b228b63333db1ee84bf
Source0:        https://github.com/kubernetes/kube-openapi/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.25 vet reports non-constant fmt.Errorf strings in
# pkg/validation/validate/result.go; keep go test itself enabled. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/NYTimes/gziphandler)
BuildRequires:  go(github.com/emicklei/go-restful/v3)
BuildRequires:  go(github.com/go-openapi/jsonreference)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/packages/packagestest)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(k8s.io/gengo/v2)
BuildRequires:  go(k8s.io/gengo/v2/generator)
BuildRequires:  go(k8s.io/gengo/v2/namer)
BuildRequires:  go(k8s.io/gengo/v2/parser)
BuildRequires:  go(k8s.io/gengo/v2/types)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/utils/net)
BuildRequires:  go(k8s.io/utils/ptr)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6/schema)
BuildRequires:  go(sigs.k8s.io/yaml)

Provides:       go(k8s.io/kube-openapi) = %{version}
Provides:       go(k8s.io/kube-openapi/cmd/openapi-gen) = %{version}
Provides:       go(k8s.io/kube-openapi/cmd/openapi-gen/args) = %{version}
Provides:       go(k8s.io/kube-openapi/cmd/openapi2smd) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/aggregator) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/builder) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/builder3) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/builder3/util) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/cached) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/common) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/common/restfuladapter) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/generators) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/generators/rules) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/handler) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/handler3) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/idl) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/internal) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/internal/third_party/go-json-experiment/json) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/internal/third_party/go-json-experiment/json/internal) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/internal/third_party/go-json-experiment/json/internal/jsonflags) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/internal/third_party/go-json-experiment/json/internal/jsonopts) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/internal/third_party/go-json-experiment/json/internal/jsontest) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/internal/third_party/go-json-experiment/json/internal/jsonwire) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/internal/third_party/go-json-experiment/json/jsontext) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/internal/third_party/go-json-experiment/json/v1) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/internal/third_party/govalidator) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/openapiconv) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/schemaconv) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/schemamutation) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/spec3) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/util) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/util/jsontesting) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/util/proto) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/util/proto/testing) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/util/proto/validation) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/util/sets) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/validation/errors) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/validation/spec) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/validation/strfmt) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/validation/strfmt/bson) = %{version}
Provides:       go(k8s.io/kube-openapi/pkg/validation/validate) = %{version}

Requires:       go(github.com/NYTimes/gziphandler)
Requires:       go(github.com/emicklei/go-restful/v3)
Requires:       go(github.com/go-openapi/jsonreference)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/google/gnostic-models)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/munnerz/goautoneg)
Requires:       go(github.com/spf13/pflag)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(google.golang.org/protobuf/proto)
Requires:       go(k8s.io/gengo/v2)
Requires:       go(k8s.io/gengo/v2/generator)
Requires:       go(k8s.io/gengo/v2/namer)
Requires:       go(k8s.io/gengo/v2/types)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/utils/net)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/randfill)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6/schema)


%description
kube-openapi contains Kubernetes OpenAPI schema generation and serving support
for Go. It is used to build OpenAPI v2/v3 discovery documents from Kubernetes
API types and is required by apimachinery and client-go builds.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
