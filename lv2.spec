%define debug_package %{nil}
# "Clean files" deletes "core dump" files, such as
# %{_includedir}/lv2/core...
%global dont_clean_files 1

Name:		lv2
Version:	1.16.0
Release:	4
Summary:	Audio Plugin Standard
Group:		System/Libraries

# lv2specgen template.html is CC-AT-SA
License:	ISC
URL:		http://lv2plug.in
Source0:	http://lv2plug.in/spec/lv2-%{version}.tar.bz2
Source1:	lv2.rpmlintrc

# For eg-scope plugin -- safe to remove if we remove that sample plugin
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gtk+-2.0)

# this package replaces lv2core
Provides:	lv2core = 6.0-4
Obsoletes:	lv2core < 6.0-4
Provides:	lv2-ui = 2.4-5
Obsoletes:	lv2-ui < 2.4-5

%description
LV2 is a standard for plugins and matching host applications, mainly
targeted at audio processing and generation.

There are a large number of open source and free software synthesis
packages in use or development at this time. This API ('LV2') attempts
to give programmers the ability to write simple 'plugin' audio
processors in C/C++ and link them dynamically ('plug') into a range of
these packages ('hosts').  It should be possible for any host and any
plugin to communicate completely through this interface.

LV2 is a successor to LADSPA, created to address the limitations of
LADSPA which many hosts have outgrown.

%package devel
Summary:	API for the LV2 Audio Plugin Standard
Group:		Development/C

Requires:	%{name} = %{EVRD}
Provides:	lv2core-devel = %{EVRD}
Provides:	lv2-ui-devel = %{EVRD}

BuildRequires:	pkgconfig(sndfile) >= 1.0.0

%description devel
lv2-devel contains the lv2.h header file and headers for all of the
LV@ specification extensions and bundles.

Definitive technical documentation on LV2 plug-ins for both the host
and plug-in is contained within copious comments within the lv2.h
header file.

%package plugins
Summary:	Sample plugins for LV2
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description plugins
Sample plugins for LV2

%prep
%setup -q

%build
python ./waf configure -vv --prefix=%{_prefix} --libdir=%{_libdir} --debug --lv2dir=%{_libdir}/%{name} CC=%{__cc}
python ./waf -vv %{?_smp_mflags}

%install
DESTDIR=%{buildroot} python ./waf -vv install

# For compatibility with old releases
ln -s lv2.pc %{buildroot}%{_libdir}/pkgconfig/lv2core.pc

%files
%{_bindir}/lv2_validate
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/atom.lv2
%{_libdir}/%{name}/buf-size.lv2
%{_libdir}/%{name}/core.lv2
%{_libdir}/%{name}/data-access.lv2
%{_libdir}/%{name}/dynmanifest.lv2
%{_libdir}/%{name}/event.lv2
%{_libdir}/%{name}/instance-access.lv2
%{_libdir}/%{name}/log.lv2
%{_libdir}/%{name}/midi.lv2
%{_libdir}/%{name}/morph.lv2
%{_libdir}/%{name}/options.lv2
%{_libdir}/%{name}/parameters.lv2
%{_libdir}/%{name}/patch.lv2
%{_libdir}/%{name}/port-groups.lv2
%{_libdir}/%{name}/port-props.lv2
%{_libdir}/%{name}/presets.lv2
%{_libdir}/%{name}/resize-port.lv2
%{_libdir}/%{name}/schemas.lv2
%{_libdir}/%{name}/state.lv2
%{_libdir}/%{name}/time.lv2
%{_libdir}/%{name}/ui.lv2
%{_libdir}/%{name}/units.lv2
%{_libdir}/%{name}/urid.lv2
%{_libdir}/%{name}/uri-map.lv2
%{_libdir}/%{name}/worker.lv2

%files devel
%doc COPYING NEWS
%{_bindir}/lv2specgen.py
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_includedir}/%{name}/core
%{_datadir}/lv2specgen/
%{_libdir}/pkgconfig/lv2core.pc
%{_libdir}/pkgconfig/%{name}.pc

%files plugins
%{_libdir}/%{name}/eg-amp.lv2
%{_libdir}/%{name}/eg-fifths.lv2
%{_libdir}/%{name}/eg-metro.lv2
%{_libdir}/%{name}/eg-midigate.lv2
%{_libdir}/%{name}/eg-params.lv2
%{_libdir}/%{name}/eg-sampler.lv2
%{_libdir}/%{name}/eg-scope.lv2
