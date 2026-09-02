# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           api
%define go_import_path  github.com/openshift/api
%define commit_id       264e80a2b6e74bdab2212839a617974aa378d2e3
# The envtest suite requires external kubebuilder control-plane assets. - HNO3Miracle
%define go_test_exclude github.com/openshift/api/tests

Name:           go-github-openshift-api
Version:        0+git20260817.264e80a
Release:        %autorelease
Summary:        OpenShift API types
License:        Apache-2.0
URL:            https://github.com/openshift/api
#!RemoteAsset:  sha256:3d7535915d7a0a9dc59d18c48fe50ec0939a1c7d9ec7f03bc1d51af4b2fbbe24
Source0:        https://github.com/openshift/api/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-fix-codegen-tools-for-current-go-vet.patch
BuildOption(prep):  -n api-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/emicklei/go-restful/v3)
BuildRequires:  go(github.com/fxamacker/cbor/v2)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/jsonreference)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)

Provides:       go(github.com/openshift/api) = %{version}

Requires:       go(github.com/gogo/protobuf)
Requires:       go(golang.org/x/tools)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kube-openapi)
Requires:       go(sigs.k8s.io/yaml)

%description
This module provides the API type definitions used by OpenShift clients and
controllers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/vendor

%changelog
%autochangelog
