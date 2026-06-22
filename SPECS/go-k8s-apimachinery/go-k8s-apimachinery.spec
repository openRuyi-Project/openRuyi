# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           apimachinery
%define go_import_path  k8s.io/apimachinery
%define upstream_version  0.35.3
# managedfields tests expect api/openapi-spec/swagger.json from the full
# kubernetes repository, but the standalone apimachinery archive lacks it. - HNO3Miracle
%define go_test_exclude %{shrink:
    %{go_import_path}/pkg/util/managedfields
    %{go_import_path}/pkg/util/managedfields/internal
}

Name:           go-k8s-apimachinery
Version:        0.36.2
Release:        %autorelease
Summary:        Shared Kubernetes API machinery for Go
License:        Apache-2.0
URL:            https://github.com/kubernetes/apimachinery
#!RemoteAsset:  sha256:1543950c9875bfa87b12038c484571d573a8870df495e6f19c53abca53e5616e
Source0:        https://github.com/kubernetes/apimachinery/archive/refs/tags/v%{upstream_version}.tar.gz#/%{_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/armon/go-socks5)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fxamacker/cbor/v2)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/jsonreference)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/moby/spdystream)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/mxk/go-flowrate)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/evanphx/json-patch.v4)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)

Provides:       go(k8s.io/apimachinery) = %{version}

Requires:       go(github.com/armon/go-socks5)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/fxamacker/cbor/v2)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-openapi/jsonpointer)
Requires:       go(github.com/go-openapi/jsonreference)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/google/gnostic-models)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/josharian/intern)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/moby/spdystream)
Requires:       go(github.com/modern-go/concurrent)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(github.com/mxk/go-flowrate)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/x448/float16)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/evanphx/json-patch.v4)
Requires:       go(gopkg.in/inf.v0)
Requires:       go(gopkg.in/yaml.v3)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kube-openapi)
Requires:       go(k8s.io/utils)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/randfill)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6)
Requires:       go(sigs.k8s.io/yaml)

%description
apimachinery provides shared Kubernetes API machinery types and helpers for Go.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
