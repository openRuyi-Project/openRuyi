# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname docutils

Name:           python-%{srcname}
Version:        0.21.2
Release:        %autorelease
Summary:        Python Documentation Utilities
License:        BSD-2-Clause AND Python-2.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND LicenseRef-openRuyi-Public-Domain
URL:            https://docutils.sourceforge.net/
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Docutils is a modular system for processing documentation into useful
formats, such as HTML, XML, and LaTeX.  It uses @dfn{reStructuredText}, an
easy to use markup language, for input.

This package provides tools for converting @file{.rst} files to other formats
via commands such as @command{rst2man}, as well as supporting Python code.

%generate_buildrequires
%pyproject_buildrequires

%check

%files -f %{pyproject_files}
%doc README*
%{_bindir}/docutils
%{_bindir}/rst2html
%{_bindir}/rst2html4
%{_bindir}/rst2html5
%{_bindir}/rst2latex
%{_bindir}/rst2man
%{_bindir}/rst2odt
%{_bindir}/rst2pseudoxml
%{_bindir}/rst2s5
%{_bindir}/rst2xetex
%{_bindir}/rst2xml

%changelog
%{?autochangelog}
