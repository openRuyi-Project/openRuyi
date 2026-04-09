# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           arrow
%define go_import_path  github.com/apache/arrow
# github.com/pdevine/tensor need this specific commit - 251
%define commit_id bc219186db40ec6966eab91ee2dec24b2ebcfca1
# TODO: something fishy is going on in riscv64 - 251
%define go_test_ignore_failure 1

Name:           go-github-apache-arrow-go-arrow
Version:        0+git20260107.bc21918
Release:        %autorelease
Summary:        Official Go implementation of Apache Arrow
License:        Apache-2.0
URL:            https://github.com/apache/arrow
#!RemoteAsset
Source0:        https://github.com/apache/arrow/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}
BuildOption(check):  -skip TestReadWrite

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/flatbuffers)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(gonum.org/v1/gonum)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
# parquet
BuildRequires:  go(github.com/JohnCGriffin/overflow)
BuildRequires:  go(github.com/andybalholm/brotli)
BuildRequires:  go(github.com/apache/thrift)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/klauspost/asmfmt)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/minio/asm2plan9s)
BuildRequires:  go(github.com/minio/c2goasm)
BuildRequires:  go(github.com/zeebo/xxh3)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
# others
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)

Provides:       go(github.com/apache/arrow/go/arrow) = %{version}

Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/flatbuffers)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/pierrec/lz4/v4)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/xerrors)
Requires:       go(gonum.org/v1/gonum)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
# parquet
Requires:       go(github.com/JohnCGriffin/overflow)
Requires:       go(github.com/andybalholm/brotli)
Requires:       go(github.com/apache/thrift)
Requires:       go(github.com/golang/snappy)
Requires:       go(github.com/klauspost/asmfmt)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/minio/asm2plan9s)
Requires:       go(github.com/minio/c2goasm)
Requires:       go(github.com/zeebo/xxh3)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/tools)
# others
Requires:       go(google.golang.org/genproto/googleapis/rpc)

# The upstream import path is github.com/apache/arrow/go/arrow
# But when testing, it will not found the files
# Because if we use the same import path as upstream,
# the files will be install into github.com/apache/arrow/go/arrow/go/arrow
# So we need to add a conflict to prevent both packages from being installed
Conflicts:      go(github.com/apache/arrow/go/v18)

%description
Apache Arrow is a development platform for in-memory analytics.
It contains a set of technologies that enable big data systems to process
and move data fast.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
