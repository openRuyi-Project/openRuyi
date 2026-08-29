# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tar-split
%define go_import_path  github.com/vbatts/tar-split

Name:           go-github-vbatts-tar-split
Version:        0.12.3
Release:        %autorelease
Summary:        Pristinely disassemble and reassemble tar archives
License:        BSD-3-Clause
URL:            https://github.com/vbatts/tar-split
#!RemoteAsset:  sha256:d91f5f15618b96e763686cfc0328b93a38a7cb9510d699d23fe5809b316798d9
Source0:        https://github.com/vbatts/tar-split/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Upstream test uses %q with int args that the current go vet rejects.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/vbatts/tar-split) = %{version}

Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/stretchr/testify)

# cmd/ is the tar-split CLI pulling urfave/cli; downstream uses the library only.
%prep -a
rm -rf cmd

%description
tar-split can disassemble a tar archive into metadata and raw content and losslessly reassemble it byte-for-byte.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
