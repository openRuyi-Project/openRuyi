# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname urllib3

Name:           python-%{srcname}
Version:        2.5.0
Release:        %autorelease
License:        MIT
URL:            https://urllib3.readthedocs.io/
Summary:        HTTP library with thread-safe connection pooling
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  pytest
BuildSystem:    pyproject
BuildOption(install): -l %{srcname} +auto
%description
Urllib3 supports features left out of urllib and urllib2 libraries.  It
can reuse the same socket connection for multiple requests, it can POST files,
supports url redirection and retries, and also gzip and deflate decoding.

%generate_buildrequires
%pyproject_buildrequires

# TODO: Add tests requires.
%check



%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
