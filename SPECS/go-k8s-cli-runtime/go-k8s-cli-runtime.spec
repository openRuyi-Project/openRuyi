# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kubernetes-cli-runtime
%define go_import_path  k8s.io/cli-runtime
# OpenShift fork pinned by kubecomps' replace directive.
%define commit_id       852eec47b608fb4a06ec15af20228cf421ad92cf

Name:           go-k8s-cli-runtime
Version:        0+git20260922.852eec4
Release:        %autorelease
Summary:        Helpers for Kubernetes command-line clients
License:        Apache-2.0
URL:            https://github.com/openshift/kubernetes-cli-runtime
#!RemoteAsset:  sha256:c83adf06c2352b7ba6ca3f041d7c2f30da038fb800051d5a4c89c4cf555b5f78
Source0:        https://github.com/openshift/kubernetes-cli-runtime/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Backports for current apimachinery and client-go APIs.
# https://github.com/kubernetes/cli-runtime/commit/efe64d475096dfb118e45157a7e1a732c2ea3429
Patch1000:      1000-Use-supported-JSON-decoder.patch
# https://github.com/kubernetes/cli-runtime/commit/ee9e8f3f861931980367799d8523018dc7010ad9
Patch1001:      1001-Use-gnostic-models-types.patch
# https://github.com/kubernetes/cli-runtime/commit/7130611e271da415b1751fd83db423701fa7c725
Patch1002:      1002-Use-cmp-Diff-in-printer-tests.patch
# https://github.com/kubernetes/cli-runtime/commit/a96869e0c2be74cb5d6099987c741079484bc348
Patch1003:      1003-Adapt-shortcut-expander-calls.patch

# Legacy error formatting uses non-constant strings rejected by current vet.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/evanphx/json-patch)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/liggitt/tabwriter)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/client-go)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(sigs.k8s.io/kustomize)
BuildRequires:  go(sigs.k8s.io/yaml)

Provides:       go(k8s.io/cli-runtime) = %{version}

Requires:       go(github.com/evanphx/json-patch)
Requires:       go(github.com/google/gnostic-models)
Requires:       go(github.com/liggitt/tabwriter)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(golang.org/x/text)
Requires:       go(gopkg.in/yaml.v2)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/client-go)
Requires:       go(sigs.k8s.io/kustomize)
Requires:       go(sigs.k8s.io/yaml)

%description
This library provides resource builders, printers and command-line
options for Kubernetes clients, using the OpenShift fork selected by
kubecomps.

%prep -a
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
