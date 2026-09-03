# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kiln
%define go_import_path  github.com/thunderbottom/kiln

Name:           go-github-thunderbottom-kiln
Version:        1.0.3
Release:        %autorelease
Summary:        Secure environment variable management toolkit
License:        MIT
URL:            https://github.com/thunderbottom/kiln
#!RemoteAsset:  sha256:165e6b61f04a4b52fe6e04c9f4027a3928fb4df2e84e46ec443a03f03e248add
Source0:        https://github.com/thunderbottom/kiln/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(filippo.io/age)
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/alecthomas/kong)
BuildRequires:  go(github.com/joho/godotenv)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}/pkg/kiln) = %{version}

Requires:       go(filippo.io/age)
Requires:       go(github.com/BurntSushi/toml)
Requires:       go(github.com/alecthomas/kong)
Requires:       go(github.com/joho/godotenv)
Requires:       go(github.com/rs/zerolog)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/term)
Requires:       go(gopkg.in/yaml.v3)

%description
Kiln provides reusable Go code for encrypted, offline environment variable
management using age encryption.

%check
%go_common
%go_prep
cd %{_builddir}/go/src/%{go_import_path}
go test -v ./...

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
