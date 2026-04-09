# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-Soundex
Version:        3.05
Release:        %autorelease
Summary:        Implementation of the soundex algorithm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-Soundex
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Text-Soundex-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(if)

%description
Soundex is a phonetic algorithm for indexing names by sound, as pronounced
in English. The goal is for names with the same pronunciation to be encoded
to the same representation so that they can be matched despite minor
differences in spelling. Soundex is the most widely known of all phonetic
algorithms and is often used (incorrectly) as a synonym for "phonetic
algorithm". Improvements to Soundex are the basis for many modern phonetic
algorithms. (Wikipedia, 2007)

%prep
%setup -q -n Text-Soundex-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
