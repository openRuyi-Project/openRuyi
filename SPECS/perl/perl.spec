# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl
Version:        5.42.0
Release:        %autorelease
Summary:        Practical Extraction and Report Language
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://www.perl.org/
VCS:            git:https://github.com/Perl/perl5.git
#!RemoteAsset:  sha256:73cf6cc1ea2b2b1c110a18c14bbbc73a362073003893ffcedc26d22ebdbdd0c3
Source0:        https://www.cpan.org/src/5.0/%{name}-%{version}.tar.xz
# Use config.over to make build of perl reproducible
Source1:        config.over
Source2:        macros.perl
BuildSystem:    autotools

# Remove Errno version check
Patch0:         0001-remove-errno-check.patch

# use "lib", not %%{_lib}, for privlib, sitelib, and vendorlib

# Perl INC path (perl -V) in search order:
# - /usr/local/share/perl5            -- for CPAN     (site lib)
# - /usr/local/lib/perl5              -- for CPAN     (site arch)
# - /usr/share/perl5/vendor_perl      -- 3rd party    (vendor lib)
# - /usr/lib/perl5/vendor_perl        -- 3rd party    (vendor arch)
# - /usr/share/perl5                  -- openRuyi     (priv lib)
# - /usr/lib/perl5                    -- openRuyi     (arch lib)

# If the %%{version} is 5.42.0, then %%{perl_abi} is 5.42
%global perl_abi        %(echo '%{version}' | sed 's/^\\([^.]*\\.[^.]*\\).*/\\1/')
%global privlib         %{_prefix}/share/perl5
%global archlib         %{_prefix}/lib/perl5
%global perl_vendorlib  %{privlib}/vendor_perl
%global perl_vendorarch %{archlib}/vendor_perl

BuildRequires:  bash
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  tar
BuildRequires:  pkgconfig(zlib)

Provides:       perl(:MODULE_COMPAT_%{version})
Provides:       /bin/perl

%description
Perl is a high-level programming language with roots in C, sed, awk and shell
scripting. Perl is good at handling processes and files, and is especially
good at handling text. Perl's hallmarks are practicality and efficiency.
While it is used to do a lot of different things, Perl's most common
applications are system administration utilities and web programming.

This is a metapackage with all the Perl bits and core modules that can be
found in the upstream tarball from perl.org.

If you need only a specific feature, you can install a specific package
instead. E.g. to handle Perl scripts with %{_bindir}/perl interpreter,
install perl-interpreter package. See perl-interpreter description for more
details on the Perl decomposition into packages.

%package        devel
Summary:        Header files for use in perl development
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Unicode-3.0
Requires:       perl(ExtUtils::ParseXS)
Requires:       perl%{?_isa} = %{version}-%{release}
Requires:       perl(Devel::PPPort)
Requires:       pkgconfig(libxcrypt)

%description    devel
This package contains header files and development modules.
Most perl packages will need to install perl-devel to build.

%package        macros
Summary:        Macros for rpmbuild
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
Requires:       perl

%description macros
RPM macros that are handy when building binary RPM packages.

%prep -a
# Copy config.over to override Configure's guesses.
cp %{SOURCE1} .

%conf
# It's called configure.gnu

%build
export BUILD_BZIP2=0
BZIP2_LIB=%{_libdir}

cp -a lib savelib
# Let's build with shared libs
./configure.gnu -des \
        -Dusethreads \
        -Dcf_by='openRuyi' \
        -Doptimize="none" \
        -Dprefix=%{_prefix} \
        -Dinstallstyle=lib/perl5 \
        -Dvendorprefix=%{_prefix} \
        -Dprivlib="%{privlib}" \
        -Darchlib="%{archlib}" \
        -Dsitelib="%{_prefix}/local/share/perl5/%{perl_abi}" \
        -Dsitearch="%{_prefix}/local/lib/perl5/%{perl_abi}" \
        -Dvendorlib="%{perl_vendorlib}" \
        -Dvendorarch="%{perl_vendorarch}" \
        -Dscriptdir='%{_bindir}' \
        -Dman1dir=%{_mandir}/man1 \
        -Dman3dir=%{_mandir}/man3 \
        -Dman1ext=1perl \
        -Dman3ext=3perl \
        -Dinc_version_list=none \
        -Dlddlflags="-shared $RPM_LD_FLAGS" \
        -Dldflags="$RPM_LD_FLAGS" \
        -Dccflags="$RPM_OPT_FLAGS" \
        -Dccdlflags="-Wl,--enable-new-dtags -Wl,-E $RPM_LD_FLAGS" \
        -Duseshrplib

make %{?_smp_mflags}
# Save a copy of libperl.so and Config files
cp -p libperl.so savelibperl.so
cp -p lib/Config.pm saveConfig.pm
cp -p lib/Config_heavy.pl saveConfig_heavy.pl

# Let's cleanup and build again, this time without shared libs
make -j1 clobber
rm -rf lib
mv savelib lib

./configure.gnu -des \
        -Dusethreads \
        -Dcf_by='openRuyi' \
        -Doptimize="none" \
        -Dprefix=%{_prefix} \
        -Dinstallstyle=lib/perl5 \
        -Dvendorprefix=%{_prefix} \
        -Dprivlib="%{privlib}" \
        -Darchlib="%{archlib}" \
        -Dsitelib="%{_prefix}/local/share/perl5/%{perl_abi}" \
        -Dsitearch="%{_prefix}/local/lib/perl5/%{perl_abi}" \
        -Dvendorlib="%{perl_vendorlib}" \
        -Dvendorarch="%{perl_vendorarch}" \
        -Dscriptdir='%{_bindir}' \
        -Dman1dir=%{_mandir}/man1 \
        -Dman3dir=%{_mandir}/man3 \
        -Dman1ext=1perl \
        -Dman3ext=3perl \
        -Dinc_version_list=none \
        -Dlddlflags="-shared $RPM_LD_FLAGS" \
        -Dldflags="$RPM_LD_FLAGS" \
        -Dccflags="$RPM_OPT_FLAGS" \
        -Dccdlflags="-Wl,--enable-new-dtags -Wl,-E $RPM_LD_FLAGS"

make %{?_smp_mflags}

%install
umask 022
%make_install

install -d -m 0755 %{buildroot}%{perl_vendorarch}/auto
install -d -m 0755 %{buildroot}%{perl_vendorlib}

# %{archlib} & %{privlib} should have 0755 too
chmod 0755 %{buildroot}%{archlib}
chmod 0755 %{buildroot}%{privlib}

find %{buildroot}%{archlib}   -type d -exec chmod 0755 {} +
find %{buildroot}%{privlib}   -type d -exec chmod 0755 {} +
find %{buildroot}%{archlib}   -type f -name '*.pm' -exec chmod 0644 {} +
find %{buildroot}%{privlib}   -type f -name '*.pm' -exec chmod 0644 {} +
find %{buildroot}%{archlib}   -type f -name '*.so' -exec chmod 0755 {} +

# Install saved files
install -m 555 savelibperl.so %{buildroot}%{archlib}/CORE/libperl.so
install -m 444 saveConfig.pm %{buildroot}%{archlib}/Config.pm
install -m 444 saveConfig_heavy.pl %{buildroot}%{archlib}/Config_heavy.pl

# Install macros
mkdir -p ${RPM_BUILD_ROOT}%{_rpmmacrodir}
install -p -m 644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_rpmmacrodir}

# remove broken pm - we don't have the module
rm -f %{buildroot}%{archlib}/Pod/Perldoc/ToTk.pm
# we don't need this in here
rm -f %{buildroot}%{archlib}/CORE/libperl.a
# test CVE-2007-5116
%{buildroot}%{_bindir}/perl -e '$r=chr(128)."\\x{100}";/$r/'
# test perl-regexp-refoverflow.diff, should not crash or hang
%{buildroot}%{_bindir}/perl -e 'eval "/\\6666666666/"'

%files
%license Copying Artistic
%dir %attr(0755,root,root) %{archlib}
%dir %attr(0755,root,root) %{privlib}
%dir %attr(0755,root,root)  %{perl_vendorlib}
%dir %attr(0755,root,root)  %{perl_vendorarch}
%{_bindir}/*
%{archlib}/*
%{privlib}/*
%{_mandir}/man1/perl*
%{_mandir}/man1/*.gz
%{_mandir}/man3/*
%exclude %{archlib}/.packlist
%exclude %{archlib}/CORE/*.h
%exclude %{_mandir}/man1/h2xs*
%exclude %{_mandir}/man1/perlivp*

%files devel
%{_bindir}/h2xs
%{_mandir}/man1/h2xs*
%{_bindir}/perlivp
%{_mandir}/man1/perlivp*
%{archlib}/CORE/*.h
%dir %{privlib}/ExtUtils
%{privlib}/ExtUtils/typemap

%files macros
%{_rpmmacrodir}/macros.perl

%changelog
%autochangelog
