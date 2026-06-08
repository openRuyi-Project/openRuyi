# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           expect
%define go_import_path  golang.org/x/tools/go/expect
%define source_version  0.1.0-deprecated

Name:           go-golang-x-tools-go-expect
Version:        0.1.0~deprecated
Release:        %autorelease
Summary:        Expect marker parser for Go tests
License:        BSD-3-Clause
URL:            https://pkg.go.dev/golang.org/x/tools/go/expect
#!RemoteAsset:  sha256:8776ba051825a2e26ad04e09edcac4437f2abe14941a566a8c5be78d50ad24cf
Source0:        https://proxy.golang.org/golang.org/x/tools/go/expect/@v/v%{source_version}.zip#/%{_name}-%{version}.zip
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  unzip

Provides:       go(golang.org/x/tools/go/expect) = %{version}

Requires:       go(golang.org/x/mod)

%description
This package restores the deprecated golang.org/x/tools/go/expect import path
needed by older x/tools test helpers. It contains the marker parser used by
packagestest-style tests and is packaged separately so dependent checks can run
without relying on another OBS project.

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
mkdir -p %{_builddir}/go/src/%{go_import_path}
cp -a %{_name}-%{version}/. %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/%{go_import_path}
go test -v ./...

%files
%license %{_name}-%{version}/LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
