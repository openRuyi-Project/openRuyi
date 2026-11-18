# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           asciidoc
Version:        10.2.1
Release:        %autorelease
Summary:        Text-based document generation program
License:        GPL-2.0-or-later
URL:            https://asciidoc.org/
VCS:            git:https://github.com/asciidoc-py/asciidoc-py.git
#!RemoteAsset:  sha256:d9f13c285981b3c7eb660d02ca0a2779981e88d48105de81bb40445e60dddb83
Source0:        https://files.pythonhosted.org/packages/source/a/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Requires:       docbook-dtds
Requires:       docbook-xsl
Requires:       libxml2
Requires:       libxslt

%description
AsciiDoc is a text document format for writing notes, documentation, articles,
books, ebooks, slideshows, web pages, man pages and blogs. AsciiDoc files can
be translated to many formats including HTML, PDF, EPUB, and man pages.

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/a2x
%{_bindir}/asciidoc

%changelog
%autochangelog
