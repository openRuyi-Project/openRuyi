# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           enumer
%define go_import_path  github.com/dmarkham/enumer

Name:           enumer
Version:        1.6.3
Release:        %autorelease
Summary:        Enum method generator for Go
License:        BSD-3-Clause
URL:            https://github.com/dmarkham/enumer
#!RemoteAsset:  sha256:b8fe84e1d938f46933110246d762c08c5cd8958291c151a9cbde581bf39dd978
Source0:        https://github.com/dmarkham/enumer/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pascaldekloe/name)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

%description
Enumer generates String, JSON, text, SQL, and related methods for typed Go
integer constants.

%package     -n go-github-dmarkham-enumer
Summary:        Go source packages for enumer
BuildArch:      noarch
Provides:       go(%{go_import_path}) = %{version}
Requires:       go(github.com/pascaldekloe/name)
Requires:       go(golang.org/x/tools)

%description -n go-github-dmarkham-enumer
This package contains the reusable Go source packages from enumer.

%build
# Keep the compiled generator outside the tree installed as Go source.
%go_common
cd %{_builddir}/go/src/%{go_import_path}
%__go build %{go_build_flags_default} -o %{_builddir}/%{_name} .

%install
install -D -m 0755 %{_builddir}/%{_name} %{buildroot}%{_bindir}/%{_name}
# The golang build system installs only the binary; also install the source subpackage.
%buildsystem_golangmodules_install

%check
# Exercise the built generator against its representative Go module fixture.
pushd %{_builddir}/go/src/%{go_import_path}/examples/gomods
%{_builddir}/%{_name} -type=Pill -json
popd
%buildsystem_golangmodules_check

%files
%doc README.md
%license LICENSE
%{_bindir}/%{_name}

%files -n go-github-dmarkham-enumer
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
