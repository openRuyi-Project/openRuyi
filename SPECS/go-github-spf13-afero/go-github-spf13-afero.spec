# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           afero
%define go_import_path  github.com/spf13/afero
%define go_test_exclude_glob %{shrink:
    github.com/spf13/afero/gcsfs*
    github.com/spf13/afero/sftpfs*
}

Name:           go-github-spf13-afero
Version:        1.15.0
Release:        %autorelease
Summary:        The Universal Filesystem Abstraction for Go
License:        Apache-2.0
URL:            https://github.com/spf13/afero
#!RemoteAsset
Source0:        https://github.com/spf13/afero/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/spf13/afero) = %{version}

Requires:       go(golang.org/x/text)

%description
Afero is a powerful and extensible filesystem abstraction system for Go.
It provides a single, unified API for interacting with diverse
filesystems—including the local disk, memory, archives, and network
storage.

Afero acts as a drop-in replacement for the standard os package,
enabling
you to write modular code that is agnostic to the underlying storage,
dramatically simplifies testing, and allows for sophisticated
architectural patterns through filesystem composition.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
