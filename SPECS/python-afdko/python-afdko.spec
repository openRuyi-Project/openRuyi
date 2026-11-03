# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname afdko

Name:           python-%{srcname}
Version:        5.0.1
Release:        %autorelease
Summary:        Adobe Font Development Kit for OpenType
License:        Apache-2.0 AND BSD-3-Clause AND HPND
URL:            https://github.com/adobe-type-tools/afdko
#!RemoteAsset:  sha256:083b504a1cd865e8bfbb42134a34318ce42ef5130daebfc5b0e2f2fb444326c5
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildSystem:    pyproject

# Accepted upstream for single-glyph and uniform-width fonts.
# https://github.com/adobe-type-tools/afdko/commit/025281e7849e42e556fc0a2e51069b757fdddef4
Patch0:         0001-prevent-underflow-when-trimming-advance-widths.patch
# AFDKO assumes antlr4_static exists, but the system ANTLR package exports
# antlr4_shared. Find ANTLR and LibXml2 at the top level so the targets
# are visible to AFDKO, and prefer antlr4_shared when available.
Patch2000:      2000-link-to-shared-system-antlr-runtime.patch

BuildOption(install):  -l %{srcname}

# scikit-build-core queries the native CMake executable before emitting wheel requirements.
BuildRequires:  cmake >= 3.16
BuildRequires:  cmake(antlr4-runtime)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  gcc-c++
BuildRequires:  python3dist(pytest)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
AFDKO builds and inspects OpenType fonts. It includes command-line tools
for compiling feature definitions, merging font programs and converting
PostScript outlines.

%prep -a
cp -p %{SOURCE1} Apache-2.0.txt
# Retain the notices from the CMap resources and the bundled PDF generator.
grep -H '^%%%%Copyright:' python/afdko/resources/Adobe-*/* \
    | sed 's|^python/afdko/resources/||' > Adobe-CMap-LICENSE.txt
grep -Fq 'Redistribution and use in source and binary forms' Adobe-CMap-LICENSE.txt
sed -n '/^---.*Licence Terms/,/^Progress Reports:/{ /^Progress Reports:/d; p; }' \
    python/afdko/pdflib/pdfgen.py > PDFgen-LICENSE.txt
grep -Fq 'ROBINSON ANALYTICS LTD. DISCLAIMS' PDFgen-LICENSE.txt
sed -i -e 's/^license = "Apache-2.0"$/license = "Apache-2.0 AND BSD-3-Clause AND HPND"/' \
    -e '/^license = /a license-files = ["LICENSE.md", "Apache-2.0.txt", "Adobe-CMap-LICENSE.txt", "PDFgen-LICENSE.txt"]' \
    pyproject.toml

%build -p
export FORCE_SYSTEM_ANTLR4=1 FORCE_SYSTEM_LIBXML2=1
export CMAKE_ARGS="-DFETCHCONTENT_FULLY_DISCONNECTED=ON"

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Exercise the tx, makeotf and mergefonts programs used to reconstruct embedded PDF fonts.
export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%{__python} -m pytest -q tests/tx_test.py tests/makeotf_test.py tests/mergefonts_test.py

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/addfeatures
%{_bindir}/afdko
%{_bindir}/buildcff2vf
%{_bindir}/buildmasterotfs
%{_bindir}/charplot
%{_bindir}/checkoutlinesufo
%{_bindir}/comparefamily
%{_bindir}/detype1
%{_bindir}/digiplot
%{_bindir}/fontplot
%{_bindir}/fontplot2
%{_bindir}/fontsetplot
%{_bindir}/hintplot
%{_bindir}/makeinstancesufo
%{_bindir}/makeotf
%{_bindir}/makeotfexe
%{_bindir}/mergefonts
%{_bindir}/otc2otf
%{_bindir}/otf2otc
%{_bindir}/otf2ttf
%{_bindir}/otfautohint
%{_bindir}/otfstemhist
%{_bindir}/rotatefont
%{_bindir}/sfntdiff
%{_bindir}/sfntedit
%{_bindir}/spot
%{_bindir}/ttfcomponentizer
%{_bindir}/ttfdecomponentizer
%{_bindir}/ttxn
%{_bindir}/tx
%{_bindir}/type1
%{_bindir}/waterfallplot

%changelog
%autochangelog
