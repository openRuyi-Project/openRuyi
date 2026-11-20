# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global majorver        25
%global minorver        0
%global securityver     5
%global patchver        0
%global buildver        8
%global newjavaver      %{majorver}.%{minorver}.%{securityver}
%global _jvmdir         %{_libdir}/jvm
%global jvm_home        %{_jvmdir}/%{name}
%global rpm_state_dir   %{_localstatedir}/lib/rpm-state/java-openjdk
# Combine the patch and build numbers in the last priority field.
%global combiver $( expr 20 '*' %{patchver} + %{buildver} )
%global alternatives_priority %( printf '%02d%02d%02d%02d' %{majorver} %{minorver} %{securityver} %{combiver} )

# Avoid the resource-intensive HotSpot LTO link; retain other distro flags.
%global _lto_cflags %{nil}

# HotSpot emits fence.i, which requires Zifencei.
%ifarch riscv64
%if "%{openruyi_riscv_arch}" == "-march=rva20u64" || "%{openruyi_riscv_arch}" == "-march=rva23u64"
%global openruyi_riscv_arch %{openruyi_riscv_arch}_zifencei
%endif
%endif

# Retain local symbols for HotSpot serviceability while RPM separates DWARF.
%global _find_debuginfo_opts -g

# Keep private JNI libraries out of the system-wide dependency namespace.
%global __provides_exclude_from ^%{_jvmdir}/
# Filter only JDK library names; retain dependencies on system libraries.
%global __requires_exclude ^lib(attach|awt|awt_headless|awt_xawt|dt_socket|extnet|fontmanager|instrument|j2gss|j2pcsc|j2pkcs11|jaas|java|javajpeg|jawt|jdwp|jimage|jli|jsig|jsound|jsvml|jvm|lcms|management|management_agent|management_ext|mlib_image|net|nio|prefs|rmi|saproc|sctp|simdsort|splashscreen|sunec|syslookup|verify|zip)[.]so([(].*[)])?$

# Recreate links after RPM removes ghost files shared by installed JDKs.
%define refresh_alternatives() %{expand:
(
for group in java javac jconsole; do
    case "$(LC_ALL=C alternatives --display "$group" 2>/dev/null)" in
        *'status is auto.'*) alternatives --auto "$group" || : ;;
        *'status is manual.'*)
            selected=$(readlink -f %{_sysconfdir}/alternatives/"$group")
            if [ -x "$selected" ]; then
                alternatives --set "$group" "$selected" || :
            fi ;;
    esac
done
:
)
}

# Keep runtime, development and monitoring tools independently selectable.
# Re-register installed OpenJDK candidates to migrate the old java followers.
%define register_alternatives() %{expand:
(
java_state=$(LC_ALL=C alternatives --display java 2>/dev/null)
javac_state=$(LC_ALL=C alternatives --display javac 2>/dev/null)
jconsole_state=$(LC_ALL=C alternatives --display jconsole 2>/dev/null)
selected_java=$(readlink -f %{_sysconfdir}/alternatives/java)
selected_javac=$(readlink -f %{_sysconfdir}/alternatives/javac)
selected_jconsole=$(readlink -f %{_sysconfdir}/alternatives/jconsole)
case "$java_state" in
    *'status is manual.'*)
        # The old followers inherit the runtime choice until they have a group.
        if [ -z "$javac_state" ]; then
            javac_state='status is manual.'
        fi
        if [ -z "$jconsole_state" ]; then
            jconsole_state='status is manual.'
        fi ;;
esac
register_group() {
    group=$1
    home=$2
    priority=$3
    [ -x "$home/bin/$group" ] || return 0
    set -- --install %{_bindir}/"$group" "$group" "$home/bin/$group" "$priority"
    if [ "$group" = java ]; then
        set -- "$@" --slave %{_jvmdir}/default-java java_home "$home"
    fi
    for tool in "$home"/bin/*; do
        [ -x "$tool" ] || continue
        tool_name=${tool##*/}
        case "$tool_name" in
            java|keytool|jfr|rmiregistry) tool_group=java ;;
            jconsole) tool_group=jconsole ;;
            *) tool_group=javac ;;
        esac
        [ "$tool_group" = "$group" ] || continue
        if [ "$tool_name" != "$group" ]; then
            set -- "$@" --slave %{_bindir}/"$tool_name" "$tool_name" "$tool"
        fi
        for manpage in "$home"/man/man1/"$tool_name".1.gz; do
            [ -f "$manpage" ] || continue
            set -- "$@" --slave %{_mandir}/man1/"${manpage##*/}" "$tool_name.1" "$manpage"
        done
    done
    alternatives "$@" || :
}
# Detach the legacy followers from java before creating their own masters.
for group in java javac jconsole; do
    while read -r candidate dash label priority; do
        case "$candidate" in
            %{_jvmdir}/java-*-openjdk/bin/java)
                [ "$dash $label" = '- priority' ] || continue
                register_group "$group" "${candidate%/bin/java}" "$priority" ;;
        esac
    done <<EOF
$java_state
EOF
    register_group "$group" %{jvm_home} %{alternatives_priority}
done
restore_group() {
    case "$2" in
        *'status is auto.'*) alternatives --auto "$1" || : ;;
        *'status is manual.'*)
            if [ -x "$3" ]; then alternatives --set "$1" "$3" || :; fi ;;
    esac
}
# Re-registration can change chkconfig's mode when a priority changes.
restore_group java "$java_state" "$selected_java"
restore_group javac "$javac_state" "$selected_javac"
restore_group jconsole "$jconsole_state" "$selected_jconsole"
:
)
}

# pretrans also runs in an empty installroot, before a shell is available.
%define snapshot_alternatives() %{expand:
local state_dir = "%{rpm_state_dir}"
local function snapshot(group, inherited_mode)
    os.remove(state_dir .. "/" .. group .. "-auto")
    os.remove(state_dir .. "/" .. group .. "-manual")
    local state = io.open("%{_localstatedir}/lib/alternatives/" .. group)
    local mode = inherited_mode
    if state then
        mode = state:read("*l")
        state:close()
    end
    if mode ~= "auto" and mode ~= "manual" then return nil end
    local path = ""
    for component in state_dir:gmatch("[^/]+") do
        path = path .. "/" .. component
        posix.mkdir(path)
    end
    local target = posix.readlink("%{_sysconfdir}/alternatives/" .. group)
    if mode == "manual" and not target then return mode end
    if target and target:sub(1, 1) ~= "/" then
        target = "%{_sysconfdir}/alternatives/" .. target
    end
    local saved = io.open(state_dir .. "/" .. group .. "-" .. mode, "w")
    if saved then
        if mode == "manual" then saved:write(target, string.char(10)) end
        saved:close()
    end
    return mode
end
local java_mode = snapshot("java")
local inherited_mode = java_mode == "manual" and "manual" or nil
snapshot("javac", inherited_mode)
snapshot("jconsole", inherited_mode)
}

# An old monolithic postun may unregister the selected runtime during upgrade.
%define restore_alternatives() %{expand:
(
for group in java javac jconsole; do
    if [ -f %{rpm_state_dir}/"$group-auto" ]; then
        alternatives --auto "$group" && rm -f %{rpm_state_dir}/"$group-auto"
    elif [ -s %{rpm_state_dir}/"$group-manual" ]; then
        IFS= read -r selected < %{rpm_state_dir}/"$group-manual"
        if [ -x "$selected" ]; then
            alternatives --set "$group" "$selected" && rm -f %{rpm_state_dir}/"$group-manual"
        else
            rm -f %{rpm_state_dir}/"$group-manual"
        fi
    fi
done
:
)
}

%bcond bootstrap        1

Name:           java-25-openjdk
Version:        %{newjavaver}.%{buildver}
Release:        %autorelease
Summary:        OpenJDK 25 Development Kit
License:        GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://openjdk.org
VCS:            git:https://github.com/openjdk/jdk25u
#!RemoteAsset:  sha256:e4cc23905feaec9d91033262d4f36a2932e145f80ed66638d61ab522f89ed8b1
Source0:        https://github.com/openjdk/jdk%{majorver}u/archive/refs/tags/jdk-%{newjavaver}+%{buildver}.tar.gz
%if %{with bootstrap}
#!RemoteAsset:  sha256:3fc35759502b620f010a9cd2b3da8454f8a49a156ceaebb00de1fd8335682d40
Source1:        https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25%2B36/OpenJDK25U-jdk_riscv64_linux_hotspot_25_36.tar.gz
#!RemoteAsset:  sha256:ee04de95ab9da7287d40bd2173076ecc2a6dd662f007bedfc6eb0380c0ef90e8
Source2:        https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25%2B36/OpenJDK25U-jdk_x64_linux_hotspot_25_36.tar.gz
%endif

# CVE-2026-91403: backport JDK-8395142 from jdk-25.0.5.0.2-ga.
# Upstream: https://github.com/openjdk/jdk25u/commit/1a8a646ef3c8f5ad2f766d43114847a2ee31cf41
Patch0:         1000-CA-Enhancements.patch

BuildRequires:  findutils
BuildRequires:  elfutils
BuildRequires:  gzip
BuildRequires:  fonts-dejavu
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  zip
BuildRequires:  pkgconfig
%if %{without bootstrap}
BuildRequires:  java-25-openjdk-devel
%endif
Provides:       java = %{version}-%{release}
Provides:       java-openjdk = %{version}-%{release}
Provides:       jre = %{version}-%{release}
# Preserve the complete JDK when upgrading the former monolithic package.
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-jmods%{?_isa} = %{version}-%{release}
Requires:       %{name}-src%{?_isa} = %{version}-%{release}
Requires:       %{name}-demo%{?_isa} = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(posttrans): update-alternatives

%description
The complete OpenJDK development kit, including the desktop runtime,
development tools, packaged modules, source archive, and demonstrations.
Install the headless or devel subpackage for a smaller installation.

%package headless
Summary:        OpenJDK %{majorver} headless runtime environment
Provides:       java-headless = %{version}-%{release}
Provides:       java-openjdk-headless = %{version}-%{release}
Provides:       jre-headless = %{version}-%{release}
Requires:       fontconfig
Requires:       fonts-dejavu
Requires(post): coreutils
Requires(postun): coreutils
Requires(posttrans): coreutils
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(posttrans): update-alternatives

%description headless
The OpenJDK runtime environment without desktop and audio libraries.
The default-java link in the JVM directory follows the selected Java runtime.

%package devel
Summary:        OpenJDK %{majorver} development tools
Provides:       java-devel = %{version}-%{release}
Provides:       java-openjdk-devel = %{version}-%{release}
Provides:       java-sdk = %{version}-%{release}
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(posttrans): update-alternatives

%description devel
The OpenJDK compiler, command-line development tools, and JNI headers.
Install the jmods subpackage to create custom runtimes with jlink.

%package jmods
Summary:        OpenJDK %{majorver} packaged modules
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}

%description jmods
Packaged OpenJDK modules for creating custom runtimes with jlink.

%package src
Summary:        OpenJDK %{majorver} Java source archive
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}

%description src
The Java source archive for the OpenJDK class libraries.

%package demo
Summary:        OpenJDK %{majorver} demonstration programs
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description demo
Demonstration programs and examples for the OpenJDK development kit.

%prep
%autosetup -p1 -n jdk25u-jdk-%{newjavaver}-%{buildver}

%build
%if %{with bootstrap}
%ifarch riscv64
tar -xf %{SOURCE1} -C %{_tmppath}
BOOTJDKPATH=%{_tmppath}/jdk-25+36
%endif
%ifarch x86_64
tar -xf %{SOURCE2} -C %{_tmppath}
BOOTJDKPATH=%{_tmppath}/jdk-25+36
%endif
%else
BOOTJDKPATH=%{_jvmdir}/java-25-openjdk
%endif

echo "$BOOTJDKPATH"

# JDK configure ignores CFLAGS/CXXFLAGS/LDFLAGS from the environment.
jdk_cflags="%{build_cflags}"
jdk_cxxflags="%{build_cxxflags}"

mkdir -p build-release
pushd build-release
bash ../configure \
    --with-version-patch=%{patchver} \
    --with-version-build=%{buildver} \
    --with-version-pre= \
    --with-version-opt= \
    --with-boot-jdk=$BOOTJDKPATH \
    --with-debug-level=release \
    --with-native-debug-symbols=external \
    --with-extra-cflags="$jdk_cflags" \
    --with-extra-cxxflags="$jdk_cxxflags" \
    --with-extra-ldflags="%{build_ldflags}" \
    --with-vendor-version-string=openRuyi \
    --with-vendor-name="openRuyi" \
    --with-vendor-url="%{_vendor_url}" \
    --with-vendor-bug-url="%{_vendor_bug_url}" \
    --enable-unlimited-crypto \
    --disable-warnings-as-errors
make images
popd

%install
mkdir -p %{buildroot}%{_jvmdir}
cp -a build-release/images/jdk %{buildroot}%{jvm_home}
# Some image configurations keep packaged modules outside the JDK image.
if [ ! -d %{buildroot}%{jvm_home}/jmods ]; then
    cp -a build-release/images/jmods %{buildroot}%{jvm_home}/jmods
fi

# External symbols keep DWARF out of JMODs. Reassemble the installed ELF files
# so RPM can generate debuginfo, debugsource and build-id links normally.
# Newer JDKs put external symbols only in the separate symbols image.
if [ -d build-release/images/symbols ]; then
    cp -a build-release/images/symbols/. %{buildroot}%{jvm_home}/
fi
test -s %{buildroot}%{jvm_home}/lib/server/libjvm.debuginfo
find %{buildroot}%{jvm_home} -type f -name '*.debuginfo' | while IFS= read -r debuginfo; do
    binary=${debuginfo%.debuginfo}
    if [ ! -f "$binary" ]; then
        binary=$binary.so
    fi
    eu-unstrip -o "$binary.unstripped" "$binary" "$debuginfo"
    mv "$binary.unstripped" "$binary"
    chmod 0755 "$binary"
    rm "$debuginfo"
done
# find-debuginfo only examines executable ELF files, including shared libraries.
find %{buildroot}%{jvm_home} -type f -name '*.so' -exec chmod 0755 {} +

# Compress versioned manuals before creating the alternatives ghost entries.
if [ -d %{buildroot}%{jvm_home}/man ]; then
    find %{buildroot}%{jvm_home}/man -type f -name '*.1' -exec gzip -9n {} +
fi

mkdir -p %{buildroot}%{rpm_state_dir} %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
touch %{buildroot}%{_jvmdir}/default-java

# List each payload once, including directories and editable configuration.
for package in headless desktop devel jmods src demo; do
    : > "$package.files"
done
find %{buildroot}%{jvm_home} -print | LC_ALL=C sort | while IFS= read -r file; do
    path=${file#%{buildroot}}
    relative=${path#%{jvm_home}}
    case "$relative" in
        /jmods|/jmods/*) package=jmods ;;
        /demo|/demo/*) package=demo ;;
        /include|/include/*|/lib/ct.sym|/lib/libsaproc.so) package=devel ;;
        /lib/src.zip) package=src ;;
        /lib/libawt_xawt.so|/lib/libjawt.so|/lib/libsplashscreen.so|/lib/libjsound.so)
            package=desktop ;;
        /bin/*|/man/man1/*)
            tool=${relative##*/}
            tool=${tool%%.1*}
            case "$tool" in
                java|keytool|jfr|rmiregistry) package=headless ;;
                jconsole) package=desktop ;;
                *) package=devel ;;
            esac ;;
        *) package=headless ;;
    esac
    if [ -d "$file" ] && [ ! -L "$file" ]; then
        entry="%%dir $path"
    elif [ "${relative#/conf/}" != "$relative" ]; then
        entry="%%config(noreplace) $path"
    else
        entry=$path
    fi
    printf '%s\n' "$entry" >> "$package.files"
    case "$relative" in
        /bin/*)
            link=%{_bindir}/${relative##*/}
            touch "%{buildroot}$link"
            printf '%s\n' "%%ghost $link" >> "$package.files" ;;
        /man/man1/*)
            link=%{_mandir}/man1/${relative##*/}
            touch "%{buildroot}$link"
            # brp-compress also reads ghost placeholders, so use valid gzip.
            gzip -9nc < /dev/null > "%{buildroot}$link"
            printf '%s\n' "%%ghost $link" >> "$package.files" ;;
    esac
done
printf '%s\n' "%%ghost %{_jvmdir}/default-java" >> headless.files

%check
build-release/images/jdk/bin/java -version
build-release/images/jdk/bin/javac -version

cat > build-release/PackagingSmoke.java <<'EOF'
import java.awt.image.BufferedImage;

public class PackagingSmoke {
    public static void main(String[] args) throws Exception {
        var image = new BufferedImage(8, 8, BufferedImage.TYPE_INT_RGB);
        var graphics = image.createGraphics();
        graphics.drawLine(0, 0, 7, 7);
        graphics.drawString("Java", 0, 7);
        if (graphics.getFontMetrics().stringWidth("Java") <= 0) {
            throw new AssertionError("No usable headless font");
        }
        graphics.dispose();
    }
}
EOF
build-release/images/jdk/bin/javac -d build-release build-release/PackagingSmoke.java
build-release/images/jdk/bin/java -Djava.awt.headless=true -cp build-release PackagingSmoke

# Exercise the separately packaged modules, including configurations without
# jmods in images/jdk.
rm -rf build-release/packaging-test-runtime
build-release/images/jdk/bin/jlink --module-path build-release/images/jmods \
    --add-modules java.base --output build-release/packaging-test-runtime
build-release/packaging-test-runtime/bin/java -version

# Check the RPM payload after find-debuginfo, and the native library in JMODs.
test -x %{buildroot}%{jvm_home}/lib/server/libjvm.so
eu-readelf -S %{buildroot}%{jvm_home}/lib/server/libjvm.so > build-release/runtime-sections.txt
if grep -Eq '\.(debug|zdebug)_info' build-release/runtime-sections.txt; then
    echo "Unexpected DWARF in the runtime libjvm.so" >&2
    exit 1
fi
if [ -d %{buildroot}%{_prefix}/lib/debug ]; then
    libjvm_debug=$(find %{buildroot}%{_prefix}/lib/debug -type f -name 'libjvm.so*.debug' -print -quit)
    test -n "$libjvm_debug"
    eu-readelf -S "$libjvm_debug" > build-release/debuginfo-sections.txt
    grep -Eq '\.(debug|zdebug)_info' build-release/debuginfo-sections.txt
fi
rm -rf build-release/packaging-test-jmod
build-release/images/jdk/bin/jmod extract --dir build-release/packaging-test-jmod \
    build-release/images/jmods/java.base.jmod
eu-readelf -S build-release/packaging-test-jmod/lib/server/libjvm.so > build-release/jmod-sections.txt
if grep -Eq '\.(debug|zdebug)_info' build-release/jmod-sections.txt; then
    echo "Unexpected DWARF in java.base.jmod libjvm.so" >&2
    exit 1
fi

%pretrans headless -p <lua>
%snapshot_alternatives

%pretrans devel -p <lua>
%snapshot_alternatives

%post headless
%register_alternatives

%posttrans headless
%register_alternatives
%restore_alternatives

%postun headless
if [ "$1" -eq 0 ]; then
    alternatives --remove java %{jvm_home}/bin/java || :
    %refresh_alternatives
fi

%post
%register_alternatives

%posttrans
%register_alternatives

%postun
if [ "$1" -eq 0 ]; then
    alternatives --remove jconsole %{jvm_home}/bin/jconsole || :
    %register_alternatives
fi

%post devel
%register_alternatives

%posttrans devel
%register_alternatives
%restore_alternatives

%postun devel
if [ "$1" -eq 0 ]; then
    alternatives --remove javac %{jvm_home}/bin/javac || :
    %refresh_alternatives
fi

# Also clean up candidates supplied by an unupgraded monolithic JDK.
%transfiletriggerpostun headless -- %{_jvmdir}
for group in java javac jconsole; do
    LC_ALL=C alternatives --display "$group" 2>/dev/null | \
    while read -r candidate dash label priority; do
        case "$candidate" in
            %{_jvmdir}/java-*-openjdk/bin/"$group")
                if [ "$dash $label" = '- priority' ] && [ ! -x "$candidate" ]; then
                    alternatives --remove "$group" "$candidate" || :
                fi ;;
        esac
    done
done
%register_alternatives

%files -f desktop.files

%files headless -f headless.files
%license LICENSE
%doc README.md
%dir %{_jvmdir}
%dir %{rpm_state_dir}

%files devel -f devel.files

%files jmods -f jmods.files

%files src -f src.files

%files demo -f demo.files

%changelog
%autochangelog
