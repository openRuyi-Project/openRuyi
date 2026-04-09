# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Encode-JIS2K
Version:        0.05
Release:        %autorelease
Summary:        JIS X 0212 (aka JIS 2000) Encodings
License:        Artistic-1.0
URL:            https://metacpan.org/dist/Encode-JIS2K
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DA/DANKOGAI/Encode-JIS2K-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Encode) >= 1.41
BuildRequires:  perl(ExtUtils::MakeMaker)

Requires:       perl(Encode) >= 1.41

%description
To find out how to use this module in detail, see Encode.

%prep
%setup -q -n Encode-JIS2K-%{version}

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
