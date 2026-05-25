# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           leveldb
%define go_import_path  github.com/syndtr/goleveldb
%define commit_id 126854af5e6d8295ef8e8bee3040dd8380ae72e8

Name:           go-github-syndtr-goleveldb-leveldb
Version:        0+git20220721.126854a
Release:        %autorelease
Summary:        LevelDB implementation in Go
License:        BSD-2-Clause
URL:            https://github.com/syndtr/goleveldb
#!RemoteAsset:  sha256:97137477d1483e84021a3d4ec0920f4ebceda9494e1b8758a1a81a64fb3890fe
Source0:        https://github.com/syndtr/goleveldb/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/nxadm/tail)
BuildRequires:  go(github.com/onsi/ginkgo)
BuildRequires:  go(github.com/onsi/ginkgo/config)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/tomb.v1)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/syndtr/goleveldb/leveldb) = %{version}
Provides:       go(github.com/syndtr/goleveldb/leveldb/cache) = %{version}
Provides:       go(github.com/syndtr/goleveldb/leveldb/comparer) = %{version}
Provides:       go(github.com/syndtr/goleveldb/leveldb/errors) = %{version}
Provides:       go(github.com/syndtr/goleveldb/leveldb/filter) = %{version}
Provides:       go(github.com/syndtr/goleveldb/leveldb/iterator) = %{version}
Provides:       go(github.com/syndtr/goleveldb/leveldb/journal) = %{version}
Provides:       go(github.com/syndtr/goleveldb/leveldb/memdb) = %{version}
Provides:       go(github.com/syndtr/goleveldb/leveldb/opt) = %{version}
Provides:       go(github.com/syndtr/goleveldb/leveldb/storage) = %{version}
Provides:       go(github.com/syndtr/goleveldb/leveldb/table) = %{version}
Provides:       go(github.com/syndtr/goleveldb/leveldb/testutil) = %{version}
Provides:       go(github.com/syndtr/goleveldb/leveldb/util) = %{version}

Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/golang/snappy)
Requires:       go(github.com/nxadm/tail)
Requires:       go(github.com/onsi/ginkgo)
Requires:       go(github.com/onsi/ginkgo/config)
Requires:       go(github.com/onsi/gomega)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(gopkg.in/tomb.v1)
Requires:       go(gopkg.in/yaml.v2)


%description
This package provides a LevelDB implementation written in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
