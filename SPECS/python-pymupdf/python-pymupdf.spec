# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pymupdf

Name:           python-pymupdf
Version:        1.27.2
Release:        %autorelease
Summary:        Python bindings for the MuPDF document library
License:        AGPL-3.0-or-later
URL:            https://pymupdf.readthedocs.io/en/latest/
VCS:            git:https://github.com/pymupdf/PyMuPDF
#!RemoteAsset:  sha256:37fc9cedeafb40839f86a074d4d9feab725144bdd4bbfd20308ff8957e2b10af
Source:         https://files.pythonhosted.org/packages/source/p/pymupdf/pymupdf-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  pymupdf fitz

BuildRequires:  pyproject-rpm-macros
BuildRequires:  mupdf-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  python3dist(mupdf)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(libclang)
BuildRequires:  python3dist(swig)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyMuPDF is a high performance Python library for data extraction,
analysis, conversion & manipulation of PDF (and other) documents.

%generate_buildrequires
%pyproject_buildrequires -R

%build -p
# build against system mupdf
export PYMUPDF_SETUP_MUPDF_BUILD=''
# build rebased implementation only
export PYMUPDF_SETUP_IMPLEMENTATIONS='b'

%files -f %{pyproject_files}
%license COPYING
%doc README.md
%{_bindir}/pymupdf

%changelog
%autochangelog
