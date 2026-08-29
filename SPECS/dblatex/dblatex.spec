# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dblatex
Version:        0.3.12
Release:        %autorelease
Summary:        A LaTeX-based converter for transforming DocBook XML and SGML documents into DVI, PDF, and PostScript formats.
License:        GPL-2.0-or-later AND GPL-2.0-only AND LPPL-1.3a AND LicenseRef-DMIT AND LicenseRef-openRuyi-Public-Domain
URL:            https://dblatex.sourceforge.net/
VCS:            hg:http://hg.code.sf.net/p/dblatex/dblatex
#!RemoteAsset:  sha256:16e82786272ed1806a079d37914d7ba7a594db792dc4cc34c1c3737dbd4da079
Source0:        http://downloads.sourceforge.net/%{name}/%{name}3-%{version}.tar.bz2
BuildArch:      noarch
BuildSystem:    pyproject

# https://sourceforge.net/p/dblatex/patches/12/
Patch0:         dblatex-0.3.12-replace-imp-by-importlib.patch
# https://sourceforge.net/p/dblatex/patches/13/
Patch1:         dblatex-0.3.12-adjust-submodule-imports.patch
# https://sourceforge.net/p/dblatex/feature-requests/20
Patch2:         dblatex-0.3.4-disable-debian.patch

BuildOption(install):  -L dbtexmf

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  texlive-latex
BuildRequires:  texlive-latexextra
BuildRequires:  texlive-latexrecommended
BuildRequires:  texlive-mathscience
BuildRequires:  texlive-fontsrecommended

Requires:       docbook-xsl
Requires:       libxslt
Requires:       python3
Requires:       texlive-basic
Requires:       texlive-formatsextra
Requires:       texlive-latex
Requires:       texlive-latexextra
Requires:       texlive-latexrecommended
Requires:       texlive-mathscience
Requires:       texlive-fontsrecommended

%description
dblatex is a program that transforms your SGML/XMLDocBook documents to DVI,
PostScript or PDF by translating them into pure LaTeX as a first process.
MathML 2.0 markups are supported, too. It started as a clone of DB2LaTeX.

%prep -a
# build_scripts uses install command arguments
sed -i -e "/if not(install.install_data)/i \        install.install_data = '%{_prefix}'" setup.py
sed -i -e "s|self._install_lib = .*|self._install_lib = '%{python3_sitelib}'|" setup.py

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{_docdir}/dblatex
%{_bindir}/dblatex
%{_datadir}/dblatex/
%{_mandir}/man1/dblatex.1*

%changelog
%autochangelog
