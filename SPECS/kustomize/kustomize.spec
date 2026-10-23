# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kustomize
%define go_import_path  sigs.k8s.io/kustomize

Name:           kustomize
Version:        2.0.3
Release:        %autorelease
Summary:        Customize Kubernetes YAML configuration
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/kustomize
#!RemoteAsset:  sha256:7619cf777a23cc9d10164f76249a628624cba798ef3461e3f31ae66a0e9b420f
Source0:        https://github.com/kubernetes-sigs/kustomize/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

# https://github.com/kubernetes-sigs/kustomize/commit/86c3863bc94ba681d13b047b171a217308f7c1b3
Patch1000:      1000-Use-kube-openapi-schema-types.patch

BuildOption(build):  -ldflags "-X %{go_import_path}/pkg/commands/misc.kustomizeVersion=%{version}"
# Current Go vet rejects variable format strings in this release.
BuildOption(check):  -vet=off
# Current ConfigMap and Secret structs add Immutable. The hash inputs are
# unchanged; retain their behavior tests and skip the old field-count check.
BuildOption(check):  -skip '^TestTypeStability$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/evanphx/json-patch)
BuildRequires:  go(github.com/ghodss/yaml)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/client-go)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(gopkg.in/yaml.v2)

%package     -n go-sigs-k8s-kustomize
Summary:        Go libraries for Kubernetes configuration customization
BuildArch:      noarch

Provides:       go(sigs.k8s.io/kustomize) = %{version}

Requires:       go(github.com/evanphx/json-patch)
Requires:       go(github.com/ghodss/yaml)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/spf13/cobra)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/client-go)
Requires:       go(k8s.io/kube-openapi)

%description
Kustomize customizes Kubernetes YAML manifests without templates. It
combines resources, patches and configuration overlays.

%description -n go-sigs-k8s-kustomize
This package provides the reusable Go source for Kustomize v2.

%prep -a
# The Go prep stage also copies the source into GOPATH.
rm -rf vendor %{_builddir}/go/src/%{go_import_path}/vendor

%install -a
rm -f %{_name}
%buildsystem_golangmodules_install

%check -a
%{buildroot}%{_bindir}/%{_name} version | grep -F 'KustomizeVersion:%{version}'

%files
%doc README.md
%license LICENSE
%{_bindir}/%{_name}

%files -n go-sigs-k8s-kustomize
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
