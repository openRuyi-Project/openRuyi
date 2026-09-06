# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           enumer
%define go_import_path  github.com/dmarkham/enumer

Name:           go-github-dmarkham-enumer
Version:        1.6.3
Release:        %autorelease
Summary:        Enum method generator for Go
License:        BSD-3-Clause
URL:            https://github.com/dmarkham/enumer
#!RemoteAsset:  sha256:b8fe84e1d938f46933110246d762c08c5cd8958291c151a9cbde581bf39dd978
Source0:        https://github.com/dmarkham/enumer/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pascaldekloe/name)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/pascaldekloe/name)
Requires:       go(golang.org/x/tools)

%description
Enumer generates String, JSON, text, SQL, and related methods for typed Go
integer constants while also providing its generator source module.

%package -n enumer
Summary:        Enum method generator for Go

%description -n enumer
Enumer generates methods for typed Go integer constants.

%prep -a
%go_prep

%build
%go_common
cd %{_builddir}/go/src/%{go_import_path}
%__go build %{go_build_flags_default} -o %{_builddir}/%{_name} .

%install -a
install -D -m 0755 %{_builddir}/%{_name} %{buildroot}%{_bindir}/%{_name}

%check
pushd %{_builddir}/go/src/%{go_import_path}/examples/gomods
%{_builddir}/%{_name} -type=Pill -json
popd
%buildsystem_golangmodules_check

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%files -n enumer
%{_bindir}/%{_name}

%changelog
%autochangelog
