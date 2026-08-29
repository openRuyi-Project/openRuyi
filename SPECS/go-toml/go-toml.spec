# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-toml
%define go_import_path  github.com/pelletier/go-toml

Name:           go-toml
Version:        1.9.5
Release:        %autorelease
Summary:        Command-line tools for inspecting and converting TOML
License:        MIT
URL:            https://github.com/pelletier/go-toml
#!RemoteAsset:  sha256:7ee5ee9344a5c18eebf9487782e00b2dbeaaf19be64b447a1e1d90f8aed710e8
Source0:        https://github.com/pelletier/go-toml/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(gopkg.in/yaml.v2)

%description
go-toml provides the tomll TOML linter and the tomljson and jsontoml format
conversion tools.

%package     -n go-github-pelletier-go-toml
Summary:        TOML parser and writer for Go
BuildArch:      noarch
Provides:       go(%{go_import_path}) = %{version}

%description -n go-github-pelletier-go-toml
This package contains the source for the github.com/pelletier/go-toml Go
library.

%prep -a
%go_prep

%build -a
%go_common
cd %{_builddir}/go/src/%{go_import_path}
for command in tomll tomljson jsontoml; do
    %__go build %{go_build_flags_default} -o %{_builddir}/${command} ./cmd/${command}
done

%install -a
for command in tomll tomljson jsontoml; do
    install -D -m 0755 %{_builddir}/${command} %{buildroot}%{_bindir}/${command}
done

%files
%doc README.md
%license LICENSE
%{_bindir}/tomll
%{_bindir}/tomljson
%{_bindir}/jsontoml

%files -n go-github-pelletier-go-toml
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
