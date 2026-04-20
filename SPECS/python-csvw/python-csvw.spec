# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname csvw

Name:           python-%{srcname}
Version:        3.7.0
Release:        %autorelease
Summary:        CSV on the web
License:        Apache-2.0
URL:            https://github.com/cldf/csvw
#!RemoteAsset:  sha256:869b5c761481e52c01a99fb4749b278a4b8b0db4e0fa1965a33a3441c703465b
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
a Python API to read and write relational,
tabular data according to the CSV on the Web
specification andcommandline tools for reading and validating CSVW data.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/csvw2datasette
%{_bindir}/csvw2json
%{_bindir}/csvw2markdown
%{_bindir}/csvw2sqlite
%{_bindir}/csvwdescribe
%{_bindir}/csvwvalidate

%changelog
%autochangelog
