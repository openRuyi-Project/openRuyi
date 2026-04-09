# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Devel-CallChecker
Version:        0.009
Release:        %autorelease
Summary:        Custom op checking attached to subroutines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Devel-CallChecker
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Devel-CallChecker-%{version}.tar.gz

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(DynaLoader::Functions) >= 0.001
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File) >= 1.03
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

Requires:       perl(DynaLoader::Functions) >= 0.001

%description
This module makes some new features of the Perl 5.14.0 C API available to
XS modules running on older versions of Perl. The features are centred
around the function cv_set_call_checker, which allows XS code to attach a
magical annotation to a Perl subroutine, resulting in resolvable calls to
that subroutine being mutated at compile time by arbitrary C code. This
module makes cv_set_call_checker and several supporting functions
available. (It is possible to achieve the effect of cv_set_call_checker
from XS code on much earlier Perl versions, but it is painful to achieve
without the centralised facility.)

%prep
%setup -q -n Devel-CallChecker-%{version}

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
