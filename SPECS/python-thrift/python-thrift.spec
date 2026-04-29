# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname thrift

Name:           python-%{srcname}
Version:        0.22.0
Release:        %autorelease
Summary:        Apache Thrift
License:        Apache-2.0
URL:            https://github.com/apache/thrift
#!RemoteAsset:  sha256:42e8276afbd5f54fe1d364858b6877bc5e5a4a5ed69f6a005b94ca4918fe1466
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:d315e6cdedc07c478de6992027bfb66f220886c6216fd7e9885ced30c3703646
Source1:        https://raw.githubusercontent.com/apache/thrift/v%{version}/LICENSE
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L
# No module named 'scons'
BuildOption(check):  -e thrift.TSCons
# No module named 'twisted'
BuildOption(check):  -e thrift.transport.TTwisted

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(tornado)

Requires:       python3dist(tornado)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Thrift is a lightweight, language-independent software stack
for point-to-point RPC implementation. Thrift provides clean
abstractions and implementations for data transport, data serialization,
and application level processing. The code generation system takes a simple
definition language as input and generates code across programming languages
that uses the abstracted stack to build interoperable RPC clients and servers.

%prep -a
cp %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
