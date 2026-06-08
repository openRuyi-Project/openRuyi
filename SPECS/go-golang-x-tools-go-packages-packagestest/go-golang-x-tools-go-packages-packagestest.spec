# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           packagestest
%define go_import_path  golang.org/x/tools/go/packages/packagestest
%define source_version  0.1.1-deprecated

Name:           go-golang-x-tools-go-packages-packagestest
Version:        0.1.1~deprecated
Release:        %autorelease
Summary:        Test helpers for Go package loading
License:        BSD-3-Clause
URL:            https://pkg.go.dev/golang.org/x/tools/go/packages/packagestest
#!RemoteAsset:  sha256:15792a78ef9338b2c08d5010b24211f85c4d39e8c31db316f1ca4a891605ed01
Source0:        https://proxy.golang.org/golang.org/x/tools/go/packages/packagestest/@v/v%{source_version}.zip#/%{_name}-%{version}.zip
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/expect)
BuildRequires:  unzip

Provides:       go(golang.org/x/tools/go/packages/packagestest) = %{version}

Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/tools/go/expect)

%description
packagestest provides integration test helpers for packages that exercise
golang.org/x/tools/go/packages. Kubernetes kube-openapi uses these helpers in
its generator tests, so the package is provided separately from the main
x/tools source package.

%prep
rm -rf %{_name}-%{version}
mkdir -p %{_name}-%{version}
/usr/lib/rpm/rpmuncompress -x -C %{_name}-%{version} %{SOURCE0}
cd %{_name}-%{version}
_srcdir=$(find . -type f -name go.mod -exec dirname {} \; | head -n 1)
cp -a "${_srcdir}/." ../_module
cd ..
rm -rf %{_name}-%{version}
mv _module %{_name}-%{version}
cd %{_name}-%{version}
rm -rf golang.org

%install
cd %{_name}-%{version}
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}
cp -a . %{buildroot}%{go_sys_gopath}/%{go_import_path}

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p %{_builddir}/go/src/golang.org/x
cp -a %{_datadir}/gocode/src/golang.org/x/tools %{_builddir}/go/src/golang.org/x/tools
rm -rf %{_builddir}/go/src/%{go_import_path}
mkdir -p %{_builddir}/go/src/golang.org/x/tools/go/packages
cp -a %{_name}-%{version} %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/golang.org/x/tools
go test -v %{go_import_path}

%files
%license %{_name}-%{version}/LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
