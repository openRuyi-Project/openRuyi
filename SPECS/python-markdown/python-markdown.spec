# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname markdown

Name:           python-%{srcname}
Version:        3.10.2
Release:        %autorelease
Summary:        Markdown implementation in Python
License:        BSD-3-Clause
URL:            https://python-markdown.github.io/
#!RemoteAsset:  sha256:994d51325d25ad8aa7ce4ebaec003febcce822c3f8c911e3b17c52f7f589f950
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pyyaml)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This is a Python implementation of John Gruberâ€™s Markdown. It is
almost completely compliant with the reference implementation, though
there are a few very minor differences.

%generate_buildrequires
%pyproject_buildrequires

%install -a
# process license file
PYTHONPATH=%{buildroot}%{python3_sitelib} \
  %{buildroot}%{_bindir}/markdown_py \
  LICENSE.md > LICENSE.html

%files -f %{pyproject_files}
# temporarily skip packaging docs - see also
# https://github.com/Python-Markdown/markdown/issues/621
#doc python3/build/docs/*
%license LICENSE.html LICENSE.md
%{_bindir}/markdown_py

%changelog
%autochangelog
