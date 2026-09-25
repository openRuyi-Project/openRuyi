# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           code-generator
%define go_import_path  yunion.io/x/code-generator
%define commit_id       a6851cfe4737798937f6beebc73acba3e607c8f9

Name:           yunion-code-generator
Version:        0+git20260922.a6851cf
Release:        %autorelease
Summary:        Model and Swagger code generators for Cloudpods
License:        Apache-2.0
URL:            https://github.com/yunionio/code-generator
#!RemoteAsset:  sha256:cb13dad862400383f13460d22db391a43076c104a235a590ff3dddbbe7aa4b27
Source0:        https://github.com/yunionio/code-generator/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

# https://github.com/yunionio/code-generator/pull/33
Patch2000:      2000-Reject-short-manager-names.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  make
BuildRequires:  go(github.com/go-openapi/loads)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/skratchdot/open-golang)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(k8s.io/gengo)
BuildRequires:  go(k8s.io/klog)
BuildRequires:  go(yunion.io/x/log)
BuildRequires:  go(yunion.io/x/pkg)

Requires:       go
Requires:       go-yunion-x-code-generator = %{version}

%package     -n go-yunion-x-code-generator
Summary:        Go sources for the Cloudpods code generators
BuildArch:      noarch

Provides:       go(yunion.io/x/code-generator) = %{version}

Requires:       go(github.com/go-openapi/loads)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/skratchdot/open-golang)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(golang.org/x/tools)
Requires:       go(k8s.io/gengo)
Requires:       go(k8s.io/klog)
Requires:       go(yunion.io/x/log)
Requires:       go(yunion.io/x/pkg)

%description
These tools generate Go API models and Swagger descriptions for
Cloudpods, and serve the resulting Swagger documentation.

%description -n go-yunion-x-code-generator
This package provides the reusable generators, templates and Go source
for the Cloudpods code generation tools.

%prep -a
rm -rf vendor %{_builddir}/go/src/%{go_import_path}/vendor

%build
# Upstream builds three independent commands instead of a root main package.
%go_common
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
%make_build model-api-gen swagger-gen swagger-serve

%install
install -D -m 0755 _output/bin/model-api-gen %{buildroot}%{_bindir}/model-api-gen
install -D -m 0755 _output/bin/swagger-gen %{buildroot}%{_bindir}/swagger-gen
install -D -m 0755 _output/bin/swagger-serve %{buildroot}%{_bindir}/swagger-serve
rm -rf _output
%buildsystem_golangmodules_install

%check -a
for command in model-api-gen swagger-gen swagger-serve; do
    %{buildroot}%{_bindir}/$command --help > /dev/null
done

%files
%doc README.md
%license LICENSE
%{_bindir}/model-api-gen
%{_bindir}/swagger-gen
%{_bindir}/swagger-serve

%files -n go-yunion-x-code-generator
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
