# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name            aescts
%define go_import_path   github.com/jcmturner/aescts/v2

Name:           go-github-jcmturner-aescts-v2
Version:        2.0.0
Release:        %autorelease
Summary:        AES ciphertext stealing mode for Go
License:        Apache-2.0
URL:            https://github.com/jcmturner/aescts
#!RemoteAsset:  sha256:fe4be1d56d46dd42e382fb9c80a4749f80e1ae8910f9a03ef214abaaa10d8623
Source0:        https://github.com/jcmturner/aescts/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/jcmturner/aescts/v2) = %{version}

%description
Aescts implements Kerberos-compatible AES ciphertext stealing modes for Go.

%install
pushd v2
%buildsystem_golangmodules_install
popd

%check
pushd v2
%buildsystem_golangmodules_check
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
