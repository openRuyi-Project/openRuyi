# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0
#

# avoid bootstrapping problem
%define _binary_payload w9.bzdio

%bcond  python 1

Name:           rpm
Summary:        The RPM Package Manager
License:        GPL-2.0-or-later
Version:        4.20.1
Release:        %autorelease
URL:            https://rpm.org/
VCS:            git:https://github.com/rpm-software-management/rpm.git
#!RemoteAsset:  sha256:52647e12638364533ab671cbc8e485c96f9f08889d93fe0ed104a6632661124f
Source:         https://ftp.osuosl.org/pub/rpm/releases/rpm-4.20.x/rpm-%{version}.tar.bz2
#!RemoteAsset:  git+https://github.com/rpm-software-management/rpmpgp_legacy#1.1
#!CreateArchive
Source1:        rpmpgp_legacy-1.1.tar.gz
Source2:        rpmsort
Source3:        rpmconfigcheck
Source4:        rpmconfigcheck.service

# quilt patches start here
Patch12:        localetag.diff
Patch18:        refreshtestarch.diff
Patch25:        brpcompress.diff
Patch26:        checkfilesnoinfodir.diff
Patch33:        rpmpopt.diff
Patch36:        rpmqpack.diff
Patch43:        rpm-shorten-changelog.diff
Patch46:        remove-brp-strips.diff
Patch51:        specfilemacro.diff
Patch60:        safeugid.diff
Patch61:        noprereqdeprec.diff
Patch67:        headeradddb.diff
Patch70:        fileattrs.diff
Patch71:        nomagiccheck.diff
Patch78:        headerchk2.diff
Patch85:        brp-compress-no-img.patch
Patch94:        checksepwarn.diff
Patch99:        enable-postin-scripts-error.diff
Patch102:       emptymanifest.diff
Patch103:       find-lang-qt-qm.patch
Patch117:       findsupplements.diff
Patch122:       db_conversion.diff
Patch123:       nextiteratorheaderblob.diff
Patch131:       posttrans.diff
Patch133:       zstdpool.diff
Patch135:       selinux_transactional_update.patch
Patch136:       rpmsort_reverse.diff
Patch138:       canongnu.diff
Patch139:       cmake_python_version.diff
Patch141:       0002-log-build-time-if-it-is-set-from-SOURCE_DATE_EPOCH.patch
Patch142:       0003-Error-out-on-a-missing-changelog-date.patch
Patch150:       unshare.diff
Patch151:       buildroot-symlink.diff
Patch154:       undefbuildroot.diff
Patch155:       rpm2archive.diff
Patch156:       mtime_policy_set.diff
Patch157:       cmake_fhardened.diff
Patch158:       archcheck.diff
Patch159:       emptypw.diff
Patch160:       buildsysprep.diff
# Fix rpmuncompress single-root archive detection for top-level directory
# entries stored without a trailing slash.
Patch2000:      2000-fix-rpmuncompress-handle-dir-without-slash.patch
Patch6464:      auto-config-update-aarch64-ppc64le.diff

BuildRequires:  binutils
BuildRequires:  bzip2
BuildRequires:  cmake
BuildRequires:  config
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  gzip
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  patch
BuildRequires:  perl
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(popt)
%if %{with python}
BuildRequires:  pkgconfig(python3)
%endif
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rpm-build

Provides:       rpminst

Requires:       rpm-config
Requires:       lua

%description
RPM Package Manager is the main tool for managing the software packages
of the openRuyi Linux distribution.

RPM can be used to install and remove software packages. With rpm, it
is easy to update packages.  RPM keeps track of all these manipulations
in a central database. This way it is possible to get an overview of
all installed packages.  RPM also supports database queries.

%package     -n python-rpm
Summary:        python binding for RPM
Provides:       python3-rpm
%python_provide python3-rpm
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-rpm
Thie package provides python binding for RPM

%package        devel
Summary:        Development files for librpm
Requires:       %{name}%{?_isa} = %{version}-%{release}
# for people confusing the one with the other
Recommends:     rpm-build%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(popt)

%description    devel
This package contains the RPM C library and header files.  These
development files will simplify the process of writing programs which
manipulate RPM packages and databases and are intended to make it
easier to create graphical package managers or any other tools that
need an intimate knowledge of RPM packages in order to function.

%package        build
Summary:        Tools and Scripts to create rpm packages
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       rpm:%_bindir/rpmbuild
Provides:       rpmbuild
# build essentials
Requires:       binutils
Requires:       bzip2
Requires:       coreutils
Requires:       diffutils
Requires:       dwz
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       gcc
#Requires:       gcc-PIE
Requires:       %{_prefix}/bin/gzip
Requires:       gettext-tools
Requires:       glibc-devel
Requires:       glibc-locale-base
Requires:       grep
Requires:       make
Requires:       patch
Requires:       sed
Requires:       systemd-rpm-macros
Requires:       tar
Requires:       util-linux
Requires:       which
Requires:       xz
Requires:       debugedit
Requires:       cpio
Requires:       file

%description    build
If you want to build a rpm, you need this package. It provides rpmbuild
and requires some packages that are usually required.

%package        plugin-unshare
Summary:        Rpm plugin for Linux namespace isolation functionality
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugin-unshare
Rpm plugin for Linux namespace isolation functionality.

%prep
%setup -q -n rpm-%{version}
pushd rpmio
tar xf %{SOURCE1}
ln -s rpmpgp_legacy-* rpmpgp_legacy
popd

rm -rf sqlite
%patch -P 12 -P 18
%patch -P 25 -P 26
%patch        -P 33       -P 36
%patch                   -P 43             -P 46
%patch       -P 51
%patch -P 60 -P 61                          -P 67
%patch -P 70 -P 71                    -P 78
%patch                               -P 85
%patch                    -P 94                         -P 99
%patch         -P 102 -P 103
%patch                                                  -P 117
%patch -P 122 -P 123
%patch -P 131          -P 133 -P 135 -P 136        -P 138
%patch -P 139
%patch -P 141 -P 142
%patch -P 150 -P 151 -P 154 -P 155 -P 156 -P 157 -P 158 -P 159
%patch -P 160
%patch 2000 -p1

%ifarch riscv64
%patch -P 6464
%endif

rm -f m4/libtool.m4
rm -f m4/lt*.m4

%build
export CFLAGS="%{optflags} -ffunction-sections"
export LDFLAGS="-Wl,-Bsymbolic-functions -ffunction-sections"

cpu="%{_target_cpu}"

mkdir _build
cd _build
cmake .. \
  -DRPM_HOST_SYSTEM_CPU="$cpu" \
  -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
  -DCMAKE_INSTALL_MANDIR:PATH=share/man \
  -DCMAKE_INSTALL_INFODIR:PATH=share/info \
  -DCMAKE_INSTALL_DOCDIR:PATH=%{_defaultdocdir}/%{NAME} \
  -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
  -DCMAKE_INSTALL_FULL_SYSCONFDIR:PATH=/etc \
  -DCMAKE_INSTALL_FULL_LOCALSTATEDIR:PATH=/var \
  -DCMAKE_INSTALL_SHAREDSTATEDIR:PATH=/var/lib \
  -DCMAKE_INSTALL_FULL_SHAREDSTATEDIR:PATH=/var/lib \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DRPM_VENDOR=openruyi \
  -DWITH_ARCHIVE=ON \
  -DWITH_READLINE=OFF \
  -DWITH_SELINUX=ON \
  -DWITH_SEQUOIA=OFF \
  -DWITH_LEGACY_OPENPGP=ON \
  -DENABLE_NDB=ON \
  -DENABLE_BDB_RO=ON \
  -DENABLE_SQLITE=OFF \
  -DWITH_AUDIT=OFF \
  -DWITH_DBUS=OFF \
  -DENABLE_PYTHON=%{?with_python:ON}%{?!with_python:OFF} \
  -DENABLE_TESTSUITE=OFF \
  -D__FIND_DEBUGINFO=%{_prefix}/lib/rpm/find-debuginfo \
  -D__AR:FILEPATH=ar -D__AS:FILEPATH=as \
  -D__CC:FILEPATH=gcc -D__CPP:FILEPATH="gcc -E" -D__CXX:FILEPATH=g++ \
  -D__GPG:FILEPATH=%{_prefix}/bin/gpg2 -D__AWK:FILEPATH=%{_prefix}/bin/gawk
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_prefix}/lib
mkdir -p %{buildroot}%{_prefix}/share/locale
ln -s ../share/locale %{buildroot}%{_prefix}/lib/locale
pushd _build
%make_install
popd
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}%{_prefix}/sbin
install -m 755 %{SOURCE3} %{buildroot}%{_prefix}/sbin
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system
install -m 644 %{SOURCE4} %{buildroot}%{_prefix}/lib/systemd/system/
mkdir -p %{buildroot}%{_prefix}/lib/rpm/macros.d
mkdir -p %{buildroot}%{_prefix}/lib/rpm/openruyi
for d in BUILD RPMS SOURCES SPECS SRPMS BUILDROOT ; do
  mkdir -p %{buildroot}%{_prefix}/src/packages/$d
  chmod 755 %{buildroot}%{_prefix}/src/packages/$d
done
for d in %{buildroot}%{_prefix}/lib/rpm/platform/*-linux/macros ; do
  dd=${d%%-linux/macros}
  dd=${dd##*/}
  mkdir %{buildroot}%{_prefix}/src/packages/RPMS/$dd
  chmod 755 %{buildroot}%{_prefix}/src/packages/RPMS/$dd
done
export RPM_BUILD_ROOT
rm -f %{buildroot}%{_prefix}/lib/rpmpopt
rm -rf %{buildroot}%{_mandir}/{fr,ja,ko,pl,ru,sk}
rm -f %{buildroot}%{_prefix}/share/locale/de/LC_MESSAGES/rpm.mo
rm -f %{buildroot}%{_prefix}/lib/rpm/cpanflute %{buildroot}%{_prefix}/lib/rpm/cpanflute2
install -m 755 %{SOURCE2} %{buildroot}%{_prefix}/lib/rpm
rm -f %{buildroot}%{_prefix}/lib/locale %{buildroot}%{_prefix}/lib/rpmrc
mkdir -p %{buildroot}/etc/rpm
chmod 755 %{buildroot}/etc/rpm
# remove some nonsense or non-working scripts
pushd %{buildroot}%{_prefix}/lib/rpm/
for f in rpm2cpio.sh rpm.daily rpmdiff* rpm.log rpm.xinetd freshen.sh u_pkg.sh \
         ocaml-find-provides.sh ocaml-find-requires.sh fileattrs/ocaml.attr \
         magic magic.mgc magic.mime* rpmfile *.pl javadeps brp-redhat \
         brp-strip-static-archive vpkg-provides*.sh http.req sql.req tcl.req \
         brp-sparc64-linux brp-strip-comment-note brp-java-gcjcompile
do
    rm -f $f
done
for i in %{_prefix}/share/automake-*/*; do
  if test -f "$i" && test -f "${i##*/}"; then
    rm -f "${i##*/}"
  fi
done
popd
%ifarch riscv64
install $(command -v config.guess)       %{buildroot}%{_prefix}/lib/rpm
install  -m 755 $(command -v config.sub) %{buildroot}%{_prefix}/lib/rpm
%endif

bash %{buildroot}%{_prefix}/lib/rpm/find-lang.sh %{buildroot} rpm

# disable sysuser handling for now
rm %{buildroot}%{_prefix}/lib/rpm/sysusers.sh
sed -e '/^%%__systemd_sysusers/s/^/#/' -i %{buildroot}%{_prefix}/lib/rpm/macros

%files -f %{name}.lang
%defattr(-,root,root)
%license       COPYING
%exclude %{_prefix}/lib/rpm/macros.d/macros.transaction_unshare
%exclude %{_mandir}/man8/rpm-plugin-unshare*
       /etc/rpm
       %{_bindir}/gendiff
       %{_bindir}/rpm
       %{_bindir}/rpm2archive
       %{_bindir}/rpm2cpio
       %{_bindir}/rpmdb
       %{_bindir}/rpmgraph
       %{_bindir}/rpmkeys
       %{_bindir}/rpmlua
       %{_bindir}/rpmqpack
       %{_bindir}/rpmquery
       %{_bindir}/rpmsign
       %{_bindir}/rpmverify
       %{_bindir}/rpmsort
       %{_prefix}/sbin/rpmconfigcheck
       %{_prefix}/lib/systemd/system/rpmconfigcheck.service
       %dir %{_prefix}/lib/rpm
       %{_prefix}/lib/rpm/macros
       %{_prefix}/lib/rpm/macros.d/
       %{_prefix}/lib/rpm/platform/
       %{_prefix}/lib/rpm/rpm.supp
       %{_prefix}/lib/rpm/rpmdb_*
       %{_prefix}/lib/rpm/rpmpopt-*
       %{_prefix}/lib/rpm/rpmrc
       %{_prefix}/lib/rpm/rpmsort
       %{_prefix}/lib/rpm/rpmdump
       %{_prefix}/lib/rpm/openruyi
       %{_prefix}/lib/rpm/tgpg
       %{_libdir}/rpm-plugins
       %{_libdir}/librpm.so.*
       %{_libdir}/librpmio.so.*
       %{_libdir}/librpmsign.so.*
%doc   %{_mandir}/man[18]/*.[18]*
%ghost /var/lib/rpm
%dir   %attr(755,root,root) %{_prefix}/src/packages/BUILD
%dir   %attr(755,root,root) %{_prefix}/src/packages/SPECS
%dir   %attr(755,root,root) %{_prefix}/src/packages/SOURCES
%dir   %attr(755,root,root) %{_prefix}/src/packages/SRPMS
%dir   %attr(755,root,root) %{_prefix}/src/packages/RPMS
%dir   %attr(755,root,root) %{_prefix}/src/packages/BUILDROOT
%dir   %attr(755,root,root) %{_prefix}/src/packages/RPMS/*

%files -n python-rpm
%license COPYING
%{_libdir}/python*/*

%files build
%defattr(-,root,root)
%{_prefix}/bin/rpmbuild
%{_prefix}/lib/rpm/pkgconfigdeps.sh
%{_prefix}/lib/rpm/ocamldeps.sh
%{_prefix}/lib/rpm/rpm_macros_provides.sh
%{_prefix}/lib/rpm/elfdeps
%{_prefix}/lib/rpm/rpmdeps
%{_prefix}/lib/rpm/rpmuncompress
%{_prefix}/bin/rpmspec
%{_prefix}/lib/rpm/brp-*
%{_prefix}/lib/rpm/check-*
%{_prefix}/lib/rpm/*find*
%{_prefix}/lib/rpm/fileattrs/
%{_prefix}/lib/rpm/*.prov
%{_prefix}/lib/rpm/*.req
%ifarch aarch64 ppc64le riscv64 loongarch64
%{_prefix}/lib/rpm/config.guess
%{_prefix}/lib/rpm/config.sub
%endif
%{_libdir}/librpmbuild.so.*

%files devel
%defattr(644,root,root,755)
%{_prefix}/include/rpm
%{_libdir}/librpm.so
%{_libdir}/librpmbuild.so
%{_libdir}/librpmio.so
%{_libdir}/librpmsign.so
%{_libdir}/pkgconfig/rpm.pc
%{_libdir}/cmake/rpm
%doc %{_docdir}/rpm

%files plugin-unshare
%defattr(-,root,root)
%{_prefix}/lib/rpm/macros.d/macros.transaction_unshare
%doc %{_mandir}/man8/rpm-plugin-unshare*

%changelog
%autochangelog
