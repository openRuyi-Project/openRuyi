# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           code-generator
%define go_import_path  k8s.io/code-generator
# Generated fixtures and examples do not match the packaged dependency tree. - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/cmd/validation-gen/output_tests/*
    %{go_import_path}/examples/*
}

Name:           go-k8s-code-generator
Version:        0.36.2
Release:        %autorelease
Summary:        Kubernetes code generation libraries
License:        Apache-2.0
URL:            https://github.com/kubernetes/code-generator
#!RemoteAsset:  sha256:c8e656c57b1a4d05c90157ee214f55cff94b6d9f3b5c84b50fcb657b61f37621
Source0:        https://github.com/kubernetes/code-generator/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

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
BuildRequires:  go(github.com/google/pprof)
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
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/gengo/v2)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)

Provides:       go(k8s.io/code-generator) = %{version}

Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/google/gnostic-models)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/pprof)
Requires:       go(github.com/spf13/pflag)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(golang.org/x/text)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/gengo/v2)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kube-openapi)
Requires:       go(k8s.io/utils)

%description
Kubernetes code-generator provides libraries and generators for producing
typed clients, informers, listers, and deep-copy code.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
