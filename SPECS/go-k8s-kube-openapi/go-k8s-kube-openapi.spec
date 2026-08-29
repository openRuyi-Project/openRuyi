# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kube-openapi
%define go_import_path  k8s.io/kube-openapi
%define commit_id aa012df4f4afd161d6bb3d4208d375556419a430
# OBS currently uses a validator path that rejects the generated OpenAPI v3
# default {} in test/integration with "property S is missing". The
# pkg/validation/spec tests also generate very large randomized OpenAPI
# specimens; GitHub Actions stops the package build while running
# TestGnosticConversionLargeDeterministic. The pkg/generators tests import
# the removed golang.org/x/tools/go/packages/packagestest test helper. Keep
# the rest of %check enabled.
# - HNO3Miracle
%define go_test_exclude %{shrink:
    %{go_import_path}/pkg/generators
    %{go_import_path}/pkg/validation/spec
    %{go_import_path}/test/integration
}

Name:           go-k8s-kube-openapi
Version:        0+git20260607.aa012df
Release:        %autorelease
Summary:        Kubernetes OpenAPI generation support for Go
License:        Apache-2.0
URL:            https://github.com/kubernetes/kube-openapi
#!RemoteAsset:  sha256:ad6d0778b676f68a1e24b0c0c398d11c874e3f684a350efd6cc7a40aa1bb5763
Source0:        https://github.com/kubernetes/kube-openapi/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/emicklei/go-restful/v3)
BuildRequires:  go(github.com/getkin/kin-openapi)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/jsonreference)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-task/slim-sprig/v3)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/NYTimes/gziphandler)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/expect)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(k8s.io/gengo)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)

Provides:       go(k8s.io/kube-openapi) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/emicklei/go-restful/v3)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-openapi/jsonpointer)
Requires:       go(github.com/go-openapi/jsonreference)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/go-task/slim-sprig/v3)
Requires:       go(github.com/google/gnostic-models)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/pprof)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/josharian/intern)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/modern-go/concurrent)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(github.com/munnerz/goautoneg)
Requires:       go(github.com/NYTimes/gziphandler)
Requires:       go(github.com/onsi/ginkgo/v2)
Requires:       go(github.com/onsi/gomega)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(github.com/spf13/pflag)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/tools/go/expect)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/yaml.v3)
Requires:       go(k8s.io/gengo)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/utils)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/randfill)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6)
Requires:       go(sigs.k8s.io/yaml)

%description
This package provides Kubernetes OpenAPI generation and validation support for Go.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
