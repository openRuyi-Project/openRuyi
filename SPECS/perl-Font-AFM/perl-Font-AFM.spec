# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Font-AFM
Version:        1.20
Release:        %autorelease
Summary:        Interface to Adobe Font Metrics files
License:        CHECK(GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/dist/Font-AFM
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/Font-AFM-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module implements the Font::AFM class. Objects of this class are
initialised from an AFM (Adobe Font Metrics) file and allow you to
obtain information about the font and the metrics of the various glyphs
in the font.

%prep
%setup -q -n Font-AFM-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes make_metrics README

%changelog
%autochangelog
