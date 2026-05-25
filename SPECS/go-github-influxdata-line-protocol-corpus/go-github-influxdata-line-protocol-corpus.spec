# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           line-protocol-corpus
%define go_import_path  github.com/influxdata/line-protocol-corpus
%define commit_id aa28ccfb893707f6d631a9f46ba40f50015e86f6

Name:           go-github-influxdata-line-protocol-corpus
Version:        0+git20210922.aa28ccf
Release:        %autorelease
Summary:        Test corpus for InfluxDB line protocol parsers
License:        MIT
URL:            https://github.com/influxdata/line-protocol-corpus
#!RemoteAsset:  sha256:09de8fe28213aed9fcbdfca36011b4e26d89d075430172588c98df04cbefd1ae
Source0:        https://github.com/influxdata/line-protocol-corpus/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n line-protocol-corpus-aa28ccfb893707f6d631a9f46ba40f50015e86f6
# The NaN marshal assertion fails with the packaged cmp/quicktest stack, while
# the rest of the corpus reader/value tests pass.
BuildOption(check):  -skip TestValueMarshal/NaN

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/frankban/quicktest)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  go(github.com/influxdata/line-protocol/v2)
BuildRequires:  go(github.com/influxdata/line-protocol/v2/lineprotocol)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/influxdata/line-protocol-corpus) = %{version}
Provides:       go(github.com/influxdata/line-protocol-corpus/lpcodecs) = %{version}
Provides:       go(github.com/influxdata/line-protocol-corpus/lpcorpus) = %{version}

Requires:       go(github.com/influxdata/line-protocol/v2)
Requires:       go(github.com/influxdata/line-protocol/v2/lineprotocol)


%description
This package contains a shared corpus used to test InfluxDB line protocol
encoders and decoders.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
