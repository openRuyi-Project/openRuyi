# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sio
%define go_import_path  github.com/minio/sio

Name:           go-github-minio-sio
Version:        0.5.1
Release:        %autorelease
Summary:        Go implementation of the Data At Rest Encryption (DARE) format.
License:        Apache-2.0
URL:            https://github.com/minio/sio
#!RemoteAsset:  sha256:673012fb71ec9170d8d5a8ae21ac34f083b3fab832d5c23b4b734b7e298371f8
Source0:        https://github.com/minio/sio/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)

Provides:       go(github.com/minio/minio-sio) = %{version}

%description
Secure IO

Go implementation of the Data At Rest Encryption (DARE) format.

Introduction

It is a common problem to store data securely - especially on untrusted
remote storage. One solution to this problem is cryptography. Before
data is stored it is encrypted to ensure that the data is confidential.
Unfortunately encrypting data is not enough to prevent more
sophisticated attacks. Anyone who has access to the stored data can try
to manipulate the data - even if the data is encrypted.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
