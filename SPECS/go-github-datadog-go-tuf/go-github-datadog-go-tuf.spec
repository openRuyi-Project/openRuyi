# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-tuf
%define go_import_path  github.com/DataDog/go-tuf
%define tag_version     1.1.1-0.5.2

Name:           go-github-datadog-go-tuf
Version:        1.1.1+0.5.2
Release:        %autorelease
Summary:        Go implementation of The Update Framework
License:        BSD-3-Clause
URL:            https://github.com/DataDog/go-tuf
#!RemoteAsset:  sha256:9662f30d9e6806cc716e2620a31caee4e50e3c3a8ad81cc360ebe5931e7de1fa
Source0:        https://github.com/DataDog/go-tuf/archive/v%{tag_version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Keep the rollback recovery fixture focused on rollback behavior after its
# static metadata expiration date has passed.
Patch2000:      2000-test-ignore-expiration-for-rollback-recovery-fixture.patch
# Support both the original Python TUF API and its current bootstrap argument.
Patch2001:      2001-test-support-python-tuf-7-updater-initialization.patch

BuildOption(prep):  -n %{_name}-%{tag_version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/flynn/go-docopt)
BuildRequires:  go(github.com/google/gofuzz)
BuildRequires:  go(github.com/secure-systems-lab/go-securesystemslib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/syndtr/goleveldb)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  python-unversioned-command
BuildRequires:  python3dist(tuf)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/flynn/go-docopt)
Requires:       go(github.com/secure-systems-lab/go-securesystemslib)
Requires:       go(github.com/syndtr/goleveldb)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/term)

%description
Go-tuf implements The Update Framework for securely publishing, retrieving,
and verifying software update metadata.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
