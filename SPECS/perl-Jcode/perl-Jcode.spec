# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Jcode
Version:        2.07
Release:        %autorelease
Summary:        Japanese Charset Handler
License:        CHECK(GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/dist/Jcode
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DA/DANKOGAI/Jcode-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64) >= 2.1

Requires:       perl(MIME::Base64) >= 2.1

%description
<Japanese document is now available as Jcode::Nihongo. >

%prep
%setup -q -n Jcode-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes Changes.ver0X README

%changelog
%autochangelog
