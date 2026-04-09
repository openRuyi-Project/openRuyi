# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           selfupdate
%define go_import_path  github.com/minio/selfupdate
# TODO: test need bsdiff, but we dont have it - Julian
%define go_test_exclude github.com/minio/selfupdate/internal/binarydist

Name:           go-github-minio-selfupdate
Version:        0.6.0
Release:        %autorelease
Summary:        Build self-updating Go programs
License:        Apache-2.0
URL:            https://github.com/minio/selfupdate
#!RemoteAsset
Source0:        https://github.com/minio/selfupdate/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(aead.dev/minisign)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/minio/selfupdate) = %{version}

Requires:       go(aead.dev/minisign)

%description
selfupdate: Build self-updating Go programs

Package update provides functionality to implement secure, self-updating
Go programs (or other single-file targets) A program can update itself
by
replacing its executable file with a new version.

It provides the flexibility to implement different updating user
experiences like auto-updating, or manual user-initiated updates. It
also
boasts advanced features like binary patching and code signing
verification.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
