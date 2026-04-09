# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test
%global tar_name libintl-perl

Name:           perl-libintl-perl
Version:        1.35
Release:        %autorelease
Summary:        Internationalization library for Perl, compatible with gettext
License:        GPL-3.0-or-later AND LGPL-2.0-or-later
URL:            https://metacpan.org/release/libintl-perl
#!RemoteAsset
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUIDO/%{tar_name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Alias)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(locale)
BuildRequires:  perl(POSIX)
# Optional run-time:
# TODO: enable this back
#BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(I18N::Langinfo)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Harness)
Requires:       perl(Carp)
Requires:       perl(Encode::Alias)
Requires:       perl(POSIX)

%description
The package libintl-perl is an internationalization library for Perl that
aims to be compatible with the Uniforum message translations system as
implemented for example in GNU gettext.

%conf
# No configure

%prep -a
# Remove executable permissions
find -type f -exec chmod -x {} \;
# Remove shebang lines
find lib/Locale gettext_xs \( -name '*.pm' -o -name '*.pod' \) \
    -exec sed -i -e '/^#! \/bin\/false/d' {} \;
# Delete unwanted files
rm MANIFEST

%build -p
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PERLLOCAL=1

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes Credits FAQ NEWS README README.md README-oldversions README.solaris README.win32 REFERENCES THANKS TODO
%license COPYING

%changelog
%autochangelog
