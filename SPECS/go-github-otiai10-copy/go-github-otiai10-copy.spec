# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           copy
%define go_import_path  github.com/otiai10/copy

Name:           go-github-otiai10-copy
Version:        1.14.1
Release:        %autorelease
Summary:        Copy files and directories recursively
License:        MIT
URL:            https://github.com/otiai10/copy
#!RemoteAsset:  sha256:32f7cd5dc0c182c4e5b86afe9e39bd6e9c1348f60de9c8511ff84ac1fcc295d8
Source0:        https://github.com/otiai10/copy/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.18
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/otiai10/mint)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sync/errgroup)
BuildRequires:  go(golang.org/x/sync/semaphore)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/unix)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sync/errgroup)
Requires:       go(golang.org/x/sync/semaphore)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/sys/unix)

%description
Copy files, directories, symbolic links, and file metadata with configurable
permissions, filtering, and concurrency. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
